# geometric = 9 * 8 ** (n-1)
def geometric_series(n):
    if n == 1:
        return 9
    return 8 * geometric_series(n -1)
    
#print geometric_series(1)
#print geometric_series(2)
#print geometric_series(3)
#print geometric_series(10)

# arithmetic = 15 + 5(n -1)
def arithmetic_series(n):
    if n == 1:
        return 15
    return 5 + arithmetic_series(n - 1)
    
#print arithmetic_series(1)
#print arithmetic_series(2)
#print arithmetic_series(3)
#print arithmetic_series(10)