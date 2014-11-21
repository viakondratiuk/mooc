def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    r = ()
    c = 1
    for v in aTup:
        if c % 2 == 1:
            r += (v,)
        c += 1
    return r
    
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    c = 0
    for k,v in aDict:
        print k,v
        c += len(v)
    return c
    
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    
    c = -1
    key = ''
    for l in aDict:
        if len(aDict[l]) > c:
            c = len(aDict[l])
            key = l
    return key
    
def findDivisors(a, b):
    r = ()
    for n in range(1, min(a, b) + 1):
        if a % n == 0 and b % n == 0:
            r = r + (n,)

    return r    