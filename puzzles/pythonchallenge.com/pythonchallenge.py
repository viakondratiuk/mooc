def pzl3():
    s = """sldfslfsdjfnjh"""
    #print s[0:3] + '-' + s[3:4] + '-' + s[4:7]
    l = r = m = 0
    r = ''
    for i in xrange(9, len(s)):
        if (
            s[i+1:i+8].isalpha() and 
            not s[i:i+1].isupper() and 
            s[i+1:i+4].isupper() and 
            s[i+4:i+5].islower() and
            s[i+5:i+8].isupper() and
            not s[i+8:i+9].isupper()
           ): 
            print s[i+4]
    return r
        
def pzl4():
    import re, urllib
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=93781'
    n = '93781'
    for i in xrange(100):
        u = urllib.urlopen(url)
        r = u.read()
        print 'nothing:', n, 'text:', r
        m = re.search('[0-9]+', r)
        n = str(m.group(0))        
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + n
        
def pzl5():
    import pickle, urllib
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    banner = pickle.load(urllib.urlopen(url))
    out = ''
    for row in banner:
        for i in row:
            out += i[0] * i[1]
        out += '\n'
    print out
    
def pzl6():
    import zipfile, re
    z = zipfile.ZipFile('channel.zip')
    f = '90052.txt'    
    for i in range(len(z.namelist())):
        #90052
        c = z.read(f)
        m = re.search('[0-9]+', c)
        print z.getinfo(f).comment
        f = str(m.group(0)) + '.txt'
pzl6()