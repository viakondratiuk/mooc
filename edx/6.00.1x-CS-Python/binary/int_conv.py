def int2bin(n, t):
    if t in ('sm', '1c', '2c'):
        if n > 0:
            t = 'us'            
        else:
            n = abs(n)
        n %= 128
    else:
        n %= 256

    if t == 'sm':
        return sign_magnitude(n)
    elif t == '1c':
        return one_complement(n)
    elif t == '2c':
        return two_complement(n)
    elif t == 'us':
        return conver_to_bin(n)
        
def conver_to_bin(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n / 2 
    b = (8 - len(b)) * '0' + b        

    return b            
        
def sign_magnitude(n):
    b = conver_to_bin(n)
    return '1' + b[1:]
    
def one_complement(n):
    b = conver_to_bin(n)
    res = ''
    for d in b:
        res += str(1-int(d))
        
    return res
    
def two_complement(n):
    n = one_complement(n)
    res = add_bin(n, '00000001')
    
    return res
    
def add_bin(n1, n2):
    res = ''
    carry = 0
    for b1, b2 in zip(reversed(n1), reversed(n2)):
        sum = carry
        sum += int(b1) + int(b2)
        if sum >= 2:
            sum -= 2
            carry = 1
        else:
            carry = 0
        res = str(sum) + res
    
    return res

