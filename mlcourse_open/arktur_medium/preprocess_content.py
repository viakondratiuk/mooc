#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

import json
import os
import codecs
import string
from bs4 import BeautifulSoup
from tqdm import tqdm
import nltk
import numpy as np
import pandas as pd

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

PATH_TO_DATA = '../../data/arktur_medium/'

def get_file_names(name):
    return name + ".json", name + "_stats.txt", name + "_parsed.csv"

def get_extract_file_names():
    return "test.json", "test_target.txt"

def replacer(s):
    mapping = {"\n": " ", "|": "", ":": "", "@": "at"}

    s = s.lower()
    for k, v in mapping.items():
        s = s.replace(k, v)
    return s


lmtzr = WordNetLemmatizer()
stop = set(stopwords.words("english") + list(string.punctuation))
tokenizer = RegexpTokenizer(r'\w+')
def tokenize(s):
    out = []
    
    #for w in word_tokenize(s.lower()):
    for w in tokenizer.tokenize(s.lower()):
        if w not in stop:
            w = lmtzr.lemmatize(w)
            out.append(w)
            
    return " ".join(out)

def collect_stats(url, before, after):
    try:
        left = 100 * after / float(before)
    except ZeroDivisionError:
        left = 0

    stats = map(str, (round(left, 2), url, before, after))
    if left < 50 or left >= 100:
        stats = ("! ", ) + tuple(stats)
    
    return stats

def parse_content(data):
    url = data["meta_tags"]["al:web:url"]
    title = tokenize(replacer(data["title"]))
    soup = BeautifulSoup(data["content"], 'html.parser')    
    
    article = soup.find("div", class_="postArticle-content")
    before, after = 0, 0
    if article:
        article = replacer(article.get_text(separator=" "))
        before = len(article)
        article = tokenize(article)
        after = len(article)
    
    tags = ""
    tags_ul = soup.find("ul", class_="tags")
    if tags_ul:
        tags = [replacer(tag.get_text()) for tag in tags_ul.find_all("li")]
        tags = " ".join(tag.replace(" ", "_") for tag in tags)
    
    out = [url, title, article, tags]
    stats = collect_stats(url, before, after)
    
    return ",".join(out) + "\n", ", ".join(stats) + "\n"

def parse_data(N, inp_data, out_stats, out_parsed):
    with codecs.open(os.path.join(PATH_TO_DATA, inp_data), "r", encoding="utf-8") as inp_json, \
         codecs.open(os.path.join(PATH_TO_DATA, out_stats), "w", encoding="utf-8") as out_stats, \
         codecs.open(os.path.join(PATH_TO_DATA, out_parsed), "w", encoding="utf-8") as out_parse:

        #N = 0
        for n, line in enumerate(tqdm(inp_json, total=N)):
            if n == N: break

            json_data = json.loads(line)
            out, stats = parse_content(json_data)
            out_parse.write(out)
            out_stats.write(stats)
            
def extract_target(data):
    soup = BeautifulSoup(data["content"], 'html.parser')
    target = soup.find(attrs={"data-action": "show-recommends"}).get_text()
    
    if "K" in target:
        target = float(target[:-1]) * 1000
    target = int(target)
    
    out = [str(np.log(target))]
    
    return "".join(out) + "\n"

def parse_target(inp_target, out_target):
    with codecs.open(os.path.join(PATH_TO_DATA, inp_target), "r", encoding="utf-8") as inp_json, \
         codecs.open(os.path.join(PATH_TO_DATA, out_target), "w", encoding="utf-8") as out_parse:

        #N = 0
        header = False
        for n, line in enumerate(tqdm(inp_json, total=N)):
            if n == N: break

            json_data = json.loads(line)
            out = extract_target(json_data)
            out_parse.write(out)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data", action="store")
    args = parser.parse_args()

    if args.data in ("train", "test"):
        if args.data == "train":
            N = 52699
        elif args.data == "test":
            N = 39492

        inp_data, out_stats, out_parsed = get_file_names(args.data)
        parse_data(N, inp_data, out_stats, out_parsed)
    elif args.data == "extract":
        N = 39492
        inp_target, out_target = get_extract_file_names()
        parse_target(inp_target, out_target)
        
        submission = pd.read_csv(PATH_TO_DATA + '/sample_submission.csv', index_col='id')
        submission['log_recommends'] = np.loadtxt(PATH_TO_DATA + '/test_target.txt')
        submission.to_csv(PATH_TO_DATA + '/submit/ethalon.csv')
