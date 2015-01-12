class tracer:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    def __call__(self, *args):
        self.calls += 1
        print 'call %s to %s' % (self.calls, self.func.__name__)
        self.func(*args)
        
@tracer
def spam(a, b, c):
    print a + b + c