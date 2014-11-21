def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other or x in res: break
            else: res.append(x)
    return res
    
def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)
    return res
        
            
s1, s2, s3 = 'spam', 'scam', 'slam'
print(intersect(s1, s2, s3))
print(union(s1, s2, s3))

s1 = {'a','a','b','b'}
s1.add('c')
s1.add('c')
s1.add('c')
print(s1)