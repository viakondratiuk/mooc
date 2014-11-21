def dec2fixedpoint(n):
    p = 1
    while (n * (2 ** p)) % 1 != 0:
        p += 1      
    num = int((2 ** p) * n)
    
    r = []
    if num == 0:
        r = ['0']
    while num > 0:
        r.insert(0, str(num % 2))
        num = num / 2

    for i in range(p - len(r)):
        r.insert(0, '0')
        
    return r
    
# sign = 1
# exponent = 3
# significand = 1

def dec2float(n):
    assert type(n) in (int, float)
    fixedPoint = dec2fixedpoint(n)
    scientificNotation = getScientificNotation(fixedPoint)
    print scientificNotation
    
    return getSign(n)
    
def getSign(n):
    if n < 0:
        return '1'
    return '0'
    
def getScientificNotation(n):
    e = 0

    for d in n:
        if d == '1':
            break;
        e -= 1
    
    return '1.' + ''.join(n)[abs(e) + 1:] + 'e' + str(e)
    
dec2float(0.1)