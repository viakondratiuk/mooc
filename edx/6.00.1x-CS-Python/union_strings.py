def union(s1, s2):
    '''
    accept 2 strings, both strings can be empty,
    each string doesn't have duplicates within itself, but may have
    the same letters in the both strings.
    
    this function returns one string containing letters from both strings,
    but excluding duplicates
    '''
    assert type(s1) == str and type(s2) == str
    
    if s1 == '':
        return s2
    elif s1[0] in s2:
        return union(s1[1:], s2)
    else:
        return s1[0] + union(s1[1:], s2)
        
testCases = {
    'cd' : ('', 'cd'),
    'acd' : ('a', 'acd'),
    'abcd' : ('ab', 'cd'),
    '12345678' : ('123456', '2345678'),
}

for ethalon in testCases.keys():
    if union(testCases[ethalon][0], testCases[ethalon][1]) == ethalon:
        print ethalon, ' passed'
    else:
        print ethalon, ' didn\'t passed'