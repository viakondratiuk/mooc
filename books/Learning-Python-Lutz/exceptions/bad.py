def gobad(x, y):
    return x / y
    
def gosouth(x):
    print gobad(x, 0)
    
def kaboom(x, y):
    print x + y
    
try:
    kaboom([1,2,3], 4)
    print 'next instruction'
except TypeError:
    print 'TypeError occured'
    
print 'next?'

def action2():
     print 1 + []
     
def action1():
    try:
        action2()
    except TypeError:
        print 'inner try'
        
try:
    action1()
except TypeError:
    print 'outer try'