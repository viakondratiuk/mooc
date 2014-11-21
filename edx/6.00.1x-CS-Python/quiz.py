def recLaceStrings(s1, s2):
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    return s1[0] + s2[0] + laceStrings(s1[1:], s2[1:])
    
def laceStrings(s1, s2):
    r = ''
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        r += s1[i] + s2[j]
        i += 1
        j += 1
    return r + s1[i:] + s2[j:] 
    
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[0] + s2[0] + helpLaceStrings(s1[1:], s2[1:], '')
    return helpLaceStrings(s1, s2, '')

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    return n >= 0 and (n == 0 or McNuggets(n-6) or McNuggets(n-9) or McNuggets(n-20));
    
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    power = 0
    while x / b > 0:
        power += 1
        x = x / b
    return power