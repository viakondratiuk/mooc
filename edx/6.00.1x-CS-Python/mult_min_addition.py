def recursive_add(a, b):
    if a == 0:
        return 0
    return recursive_add(a - 1, b) + b
    
print recursive_add(5, 12)

print 2 >> 1