# README
# - Это рабочая версия, все предыдущие посылки не учитывать
# - Все файлы должны быть в той же директории, что и этот скрипт
# - Для работы скрипта нужно поставить несколько nltk библиотек (stopwords, punctuation, WordNetLemmatizer). Просто решать ошибки одна за другой, копирую и выполняя указанные команды.


# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json
import os
from sklearn.metrics import mean_absolute_error
from datetime import datetime
from tqdm import tqdm
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import codecs

# In[2]:

os.chdir("/notebooks/jupyter_notebooks/arktur_medium_submit")
print(os.getcwd())

INP_TRAIN = "train.json"
INP_TEST  = "test.json"
OUT_TRAIN = "train.vw"
OUT_TEST = "test.vw"
LOG = True


# In[3]:


# remove html tags

from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ' '.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


# In[4]:


train_target = pd.read_csv('train_log1p_recommends.csv', index_col='id')


# In[5]:


# transform data to vw format

lmtzr = WordNetLemmatizer()
stop = set(stopwords.words("english") + list(string.punctuation) + ["’", "“", "”"])
tokenize = lambda s: " ".join(lmtzr.lemmatize(i) for i in word_tokenize(s.lower()) if i not in stop)


def to_vw(data, label):
    exclude = set(string.punctuation)
       
    content = strip_tags(data["content"]).replace("\n", " ").replace(":", "").replace("|", "")
    content = tokenize(content)
    
    title = strip_tags(data["title"]).replace("\n", " ").replace(":", "").replace("|", "")
    title = tokenize(title)
    
    author = strip_tags(data["meta_tags"]["author"]).replace("\n", " ").replace(":", "").replace("|", "")
    author = "".join(ch for ch in author if ch not in exclude).replace(" ", "_").lower()
    
    domain = data["domain"].replace("\n", " ").replace(":", "").replace("|", "").lower()
    
    # date time
    dt = datetime.strptime(data["published"]["$date"][:-1], "%Y-%m-%dT%H:%M:%S.%f")
    month = dt.month
    weekday = dt.weekday()
    hour = dt.hour 
    read_time = data["meta_tags"]["twitter:data1"].split(" ")[0]
    read_time = read_time if read_time else 0.1
    
    # binary
    is_weekend = 1 if weekday in (5, 6) else 0
    is_night = 1 if hour in range(0, 7) else 0
    is_morning = 1 if hour in range(7, 12) else 0
    is_noon = 1 if hour in range(12, 19) else 0
    is_eve = 1 if hour in range(19, 24) else 0
    is_image = 1 if data["image_url"] else 0


    out = [
        str(np.log(label)),
        "a_content %s" % content,
        "b_author %s" % author,
        "c_title %s" % title,
        "d_domain %s" % domain,
        "e_num 10:%s 11:%s 12:%s 13:%s" % (month, weekday + 1, hour + 1, read_time),
        "f_binary 0:%s 1:%s 2:%s 3:%s 4:%s 5:%s" % 
        (is_weekend, is_night, is_morning, is_noon, is_eve, is_image)
    ]
    
    return str(" |".join(out).encode('ascii', 'ignore').strip())[2:-1] + "\n"


# In[7]:


with codecs.open(INP_TRAIN, encoding="utf-8") as inp_json, codecs.open(OUT_TRAIN, 'w', encoding="utf-8") as out_train:
    N = 52699
    #N = 10
    header = False
    
    for n, json_ in enumerate(tqdm(inp_json, total=N)):
        if n == N: break

        json_data = json.loads(json_)
        label = train_target.iloc[n]["log_recommends"]
        out = to_vw(json_data, label)
        out_train.write(out)

# In[12]:


os.system('vw -d train.vw -k --cache_file=medium.cache --loss_function squared --ngram=2 --passes 5 -b 24 -l 0.5 --power_t=0.5 --l2=1e-5 -f model.vw --quiet')


# In[17]:


# create test data

import codecs

with codecs.open(INP_TEST, encoding="utf-8") as inp_json, codecs.open(OUT_TEST, 'w', encoding="utf-8") as out_test:
    N = 39492        
    #N = 10
    for n, json_ in enumerate(tqdm(inp_json, total=N)):
        if n == N: break

        json_data = json.loads(json_)

        out = to_vw(json_data, 1)
        out_test.write(out)


# In[18]:


# predict for test

os.system('vw -i model.vw -t -d test.vw -p test_predictions.txt --quiet')


# In[19]:


# create submission

submission = pd.read_csv('sample_submission.csv', index_col='id')
if LOG:
    submission['log_recommends'] = np.exp(np.loadtxt('test_predictions.txt'))
else:
    submission['log_recommends'] = np.loadtxt('test_predictions.txt')
# submission.to_csv(PATH_TO_DATA + '/submit/best_n2_p5_b24_l05_p05_l2_1e5.csv')
submission.to_csv('best_prediction.csv')

