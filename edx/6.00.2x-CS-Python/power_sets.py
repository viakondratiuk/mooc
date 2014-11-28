'''
Power Set of 2 bags combination [A,B,C]:
1.     [], []
2.     [A], []
3.     [B], []
4.     [C], []
5.     [], [A]
6.     [], [B]
7.     [], [C]
8.     [A,B], []
9.     [A,C], []
10.    [B,C], []
11.    [], [A,B]
12.    [], [A,C]
13.    [], [B,C]
14.    [A,B,C], []
15.    [], [A,B,C]
16.    [A,B], [C]
17.    [A,C], [B]
18.    [B,C], [A]
19.    [C], [A,B]
20.    [B], [A,C]
21.    [A], [B,C]
22.    [A], [B]
23.    [A], [C]
24.    [B], [A]
25.    [B], [C]
26.    [C], [A]
27.    [C], [B]

not A
1. [], []
2. [B], []
3. [C], []
4. [], [B]
5. [], [C]
6. [B,C], []
7. [], [BC]
8. [C], [B]
9. [B], [C]
'''

def powerSetTwoBags(items):
    itemsCnt = len(items)    
    comb = 2 ** itemsCnt
    res = []
    for l1 in xrange(comb):
        for l2 in xrange(comb):
            bag1 = []
            bag2 = []
            if l1 & l2 == 0:
                bin1 = bin(l1)[2:].zfill(itemsCnt)
                bin2 = bin(l2)[2:].zfill(itemsCnt)
                print bin1, bin2
                bag1 = [items[i1] for i1 in xrange(itemsCnt) if bin1[i1] == '1']
                bag2 = [items[i2] for i2 in xrange(itemsCnt) if bin2[i2] == '1']
                res.append([bag1, bag2])
    return res
    
def powerSetTwoBagsSmart(items):
    N = len(items)
    res = []
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            print '(i / 3**j)=','('+str(i)+'/ 3**'+str(j)+') % 3=',(i / 3**j) % 3
            if (i / 3**j) % 3 == 1 and j in (0,1):                
                bag1.append(items[j])
            elif (i / 3**j) % 3 == 2 and j in (0,1):
                bag2.append(items[j])
        print '-------------'
        res.append([bag1, bag2])
    return res
    
ps = powerSetTwoBagsSmart(['A','B','C'])
print 'Power Set length is:', len(ps)
for i, p in enumerate(ps):
    print i, p