def hash_str(s, tableSize = 101):
    number = ''
    for c in s:
        number = number + str(ord(c))

    return int(number) % tableSize
    
#print hash_str('some long string')
#print hash_str('a')
#print hash_str('b')
#print hash_str('s1ome long aaa')

#Simulate a collision
'''
print hash_str('Eric', 7)
print hash_str('Chris', 7)
print hash_str('Sarina', 7)
print hash_str('Jill', 7)
'''

import random

class intDict(object):
    def __init__(self, numBuckets):
        self.buckets = []
        self.numBuckets = numBuckets
        for i in xrange(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, dictKey, dictVal):
        bucketKey = dictKey % self.numBuckets
        hashBucket = self.buckets[bucketKey]
        for i in xrange(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))
        
    def getValue(self, dictKey):
        bucketKey = dictKey % self.numBuckets
        hashBucket = self.buckets[bucketKey]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
        
    def __str__(self):
        res = '{'
        for b in self.buckets:
            for t in b:
                res = res + str(t[0]) + ':' + str(t[1]) + ','
        return res[:-1] + '}'
        
D = intDict(10)

for i in xrange(20):
    key = random.choice(xrange(10 ** 5))
    D.addEntry(key, i)
    
print 'The buckets are:'
for hashBucket in D.buckets:
    print '  ', hashBucket

print 'Average bucket length: ', sum(map(len, D.buckets)) / float(D.numBuckets)
print 'Max bucket length: ', max(map(len, D.buckets))