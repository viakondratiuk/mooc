a, b, x, y, z = map(int, '6 4 7 5 3'.split())

def check_cupboard(a, b, x, y, z):
    l1, l2 = sorted([a, b]), sorted([x, y, z])
    if l1[0] > l2[0] and l1[1] > l2[1]:
        return 1
    return 0
    
print(check_cupboard(a, b, x, y, z))