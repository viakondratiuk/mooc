def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    r = 1
    while exp > 0:
        r *= base
        exp -= 1
    return r
    
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    return base* recurPower(base, exp - 1)
    
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp <= 0:
        return 1           
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    return base * recurPowerNew(base, exp - 1)    
    
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    test = min(a, b)
    while test > 0:
        if a % test == 0 and b % test == 0:
            break
        test -= 1
    return test    
    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    return gcdRecur(b, a % b)
    
def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    c = 0
    for l in aStr:
        c += 1
    return c
    
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0
    return 1 + lenRecur(aStr[1:])    
    
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
        
    midIdx = len(aStr) / 2
    midEl = aStr[midIdx]

    if char == midEl:
        return True
    elif char > midEl:
        return isIn(char, aStr[midIdx + 1:])
    elif char < midEl:
        return isIn(char, aStr[:midIdx])
        
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if str1[:1] != str2[-1:]:
        return False
    elif str1 == '' and str2 == '':
        return True
    return semordnilap(str1[1:], str2[:-1])
    
# Lections material
def hanoiTowers(s, fr, to, spare):
    def printMove(fr, to):
        print('move from ' + str(fr) + ' to ' + str(to))
    
    def moveTower(s, fr, to, spare):
        if s == 1:
            printMove(fr, to)
        else:
            moveTower(s-1, fr, spare, to)
            moveTower(1, fr, to, spare)
            moveTower(s-1, spare, to, fr)

    return moveTower(s, fr, to, spare)
    
def fib(x):
    '''assume x an int >= 0
       returns Fibbonaci of x'''
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)
    
def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        r = ''
        for l in s:
            if l in 'abcdefghijklmnopqrstuvwxyz':
                r += l
        return r
        
    def isPal(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))
    
def fibMeter(n):
    global fibCount
    fibCount += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fibMeter(n - 1) + fibMeter(n - 2)
    
def testFib():
    n = 10
    global fibCount
    fibCount = 0
    print 'Fib of ', n, ' = ', fibMeter(n)
    print 'Fib calls number ', fibCount
    
    
def minAddition(first, second):
    if second == 0:
        return 0
        
    if second % 2 == 1:
        return minAddition(first << 1, second / 2) + first
    else:
        return minAddition(first << 1, second / 2)
        