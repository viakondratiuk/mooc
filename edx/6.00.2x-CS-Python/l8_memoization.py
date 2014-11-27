def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
    
def testFib(n, fcn):
    for i in xrange(n):
        print fcn.__name__, 'number of', i, ':', fcn(i)        

def fibMemo(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    elif n in memo:
        return memo[n]
    res = fibMemo(n - 1, memo) + fibMemo(n - 2, memo)
    memo[n] = res
    return res
    
testFib(33, fib)
testFib(33, fibMemo)