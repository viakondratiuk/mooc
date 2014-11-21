'''
Actually according to thos blog post:
http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html
Tail recursion at python is not supported.
'''
def rcsv_factorial(n):
    if n <= 1:
        return 1
    return n * rcsv_factorial(n - 1)    

def tail_factorial(n, current = 1):    
    if n <= 1:
        return current
    return tail_factorial(n - 1, n * current)
    
factorial_of = 5

print rcsv_factorial(factorial_of)
print tail_factorial(factorial_of)

def rcsv_arithmetic_sum(n):
    if n == 1:
        return n
    return n + rcsv_arithmetic_sum(n - 1)
    
def tail_arithmetic_sum(n, current = 0):
    if n == 1:
        return current + 1
    return tail_arithmetic_sum(n - 1, n + current)    
    
arithmetic_sum_of = 100

print rcsv_arithmetic_sum(arithmetic_sum_of)
print tail_arithmetic_sum(arithmetic_sum_of)