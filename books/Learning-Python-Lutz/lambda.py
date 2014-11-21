f = lambda x = 10, y = 100, z = 1000: x + y + z
#print f(x = 1, z = 100)

L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]
     
for f in L:
    pass
    #print(f(3))

#print L[0](2)

# lambda function used as switch statement
# can be abad solution actually, because lambda is calculated on every dict call
key = 'first'
print {
    'first'  : (lambda x: x + 2),
    'second' : (lambda x: x + 4),
    'third'  : (lambda x: x + 8),        
}.get(key, 'key is not found')(2)

def action(x):
    return (lambda y: x + y)
    
act = action(99)
print act
print act(2)