def genPrimes():
    yield 2
    yield 3
    yield 5
    i = 6
    while True:
        isPrime = True
        j = 2
        while j < i / 2:
            if i % j == 0:
                isPrime = False
                break
            j += 1
        if isPrime:
            yield i
        i += 1
        
def genPrimes1():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
        
'''
gen = genPrimes()

print gen.next()
print gen.next()
print gen.next()
print gen.next()
print gen.next()
print gen.next()
'''

gen1 = genPrimes()
print gen1.next()
print gen1.next()
print gen1.next()
print gen1.next()
print gen1.next()
print gen1.next()