def func_decorator(F):
    print 'call func_decorator'
    return F
    
def class_decorator(C):
    print 'call class'
    return C

@func_decorator    
def func():
    print 'call func'

@class_decorator
class C: pass

func()
x = C()