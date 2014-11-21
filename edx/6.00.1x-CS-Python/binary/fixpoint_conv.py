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