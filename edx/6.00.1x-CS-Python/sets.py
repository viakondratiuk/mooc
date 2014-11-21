def isIn(e, l):
    '''
    e - element to search
    l - list in which we should search e
    Wortht case: complexity is len(l)
    '''
    for i in l:
        if i == e:
            return True
    return False
    
def isSubstr(s1, s2):
    '''
    s1 - substr to search
    s2 - list in which we should search s1
    '''
    if len(s1) == 0 and len(s2) == 0:
        return True
        
    i, j = 0, 0
    series = False
    matched = 0
    while i < len(s1):
        while j < len(s2):            
            if s1[i] == s2[j]:                
                matched += 1
                series = True               
                j += 1
                break;
            elif series:
                series = False
                matched = 0                
            j += 1
        i += 1
        if len(s1) == matched:
            return True
    return False

def genSubsets(L):
    '''
    L - list. Generate all possible subsets for this list. Complexity 2 ** len(L)
    '''
    # Return empty list
    if len(L) == 0:
        return [[]]
    
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)

    return smaller + new
    
def union(s1, s2):
    '''
    Find union of 2 strings
    s1 - list one
    s2 - list two
    '''
    if len(s1) == 0:
        return s2
    if s1[0] in s2:
        return union(s1[1:], s2)
    return s1[0] + union(s1[1:], s2)
    
def intersect(s1, s2):
    '''
    Find intesection of 2 strings
    s1 - list one
    s2 - list two
    '''
    if len(s1) == 0:
        return s1  
    if s1[0] not in s2:
        return intersect(s1[1:], s2)
    return s1[0] + intersect(s1[1:], s2)
    
def difference(s1, s2):
    '''
    Find difference of 2 strings
    s1 - list one
    s2 - list two
    '''
    if len(s1) == 0:
        return s1          
    if s1[0] in s2:
        return difference(s1[1:], s2)
    return s1[0] + difference(s1[1:], s2)