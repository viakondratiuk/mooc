def inc(x): return x + 10

c = [1, 2, 3, 4]

print map(inc, c)
print map(lambda x: x + 10, c)
print map(pow, [1,2,3], [2,3,4])

print filter(lambda x: x > 0, range(-5, 5))

print reduce((lambda x, y: x + y), [1, 2, 3, 4])
print reduce((lambda x, y: x * y), [1, 2, 3, 4])

print [x ** 2 for x in xrange(10)]
print map((lambda x: x ** 2), xrange(10))

def gen_squares(n):
    for i in xrange(n):
        yield i ** 2
        
print [i for i in gen_squares(5)]
gen = gen_squares(5)
print gen.next()
print gen.next()
print gen.next()
print gen.next()
print gen.next()

# generator expression
G = (x ** 2 for x in range(4))

print list((abs(x) for x in (-1,-2,3,4)))

def saver(x=[]):
    x.append(1)
    return x
    
print saver([2])
print saver()
print saver()
print saver()