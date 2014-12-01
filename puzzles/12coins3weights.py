w = 0

def find_anomalia(cn):
    global w
    w = 0
    c1 = compare(cn[:4], cn[4:8])
    ret = ''
    
    if c1 == 0:
        c2 = compare(cn[:3], cn[8:11])
        # Coin 11 is > or <
        if c2 == 0:
            c3 = compare(cn[3], cn[11])
            if c3 == 0:
                ret = (-1, '=')
            elif c3 == 1:
                ret = (11, '<')
            elif c3 == -1:
                ret = (11, '>')
        # Coins 8,9,10 is <
        elif c2 == 1:
            c3 = compare(cn[8], cn[9])
            if c3 == 0:
                ret = (10, '<')
            elif c3 == 1:
                ret = (9, '<')
            elif c3 == -1:
                ret = (8, '<')
        # Coins 8,9,10 is >
        elif c2 == -1:
            c3 = compare(cn[8], cn[9])
            if c3 == 0:
                ret = (10, '>')
            elif c3 == 1:
                ret = (8, '>')
            elif c3 == -1:
                ret = (9, '>')
    elif c1 == 1:
        c2 = compare([cn[0], cn[1], cn[4]], [cn[2], cn[3], cn[8]])
        # Coins 5,6,7 is <
        if c2 == 0:
            c3 = compare(cn[5], cn[6])
            if c3 == 0:
                ret = (7, '<')
            elif c3 == 1:
                ret = (6, '<')
            elif c3 == -1:
                ret = (5, '<')
        # Coins 0,1 is >
        elif c2 == 1:
            c3 = compare(cn[0], cn[1])
            if c3 == 0:
                ret = (-2, '=')
            elif c3 == 1:
                ret = (0, '>')
            elif c3 == -1:
                ret = (1, '>')
        # Coins 2,3 is >; 4 is <
        elif c2 == -1:
            c3 = compare(cn[2], cn[3])
            if c3 == 0:
                ret = (4, '<')
            elif c3 == 1:
                ret = (2, '>')
            elif c3 == -1:
                ret = (3, '>')
    elif c1 == -1:
        c2 = compare([cn[0], cn[1], cn[4]], [cn[2], cn[3], cn[8]])
        # Coins 5,6,7 is >
        if c2 == 0:
            c3 = compare(cn[5], cn[6])
            if c3 == 0:
                ret = (7, '>')
            elif c3 == 1:
                ret = (5, '>')
            elif c3 == -1:
                ret = (6, '>')
        # Coins 2,3 is <; 4 is >
        elif c2 == 1:
            c3 = compare(cn[2], cn[3])
            if c3 == 0:
                ret = (4, '>')
            elif c3 == 1:
                ret = (3, '<')
            elif c3 == -1:
                ret = (2, '<')
        # Coins 0,1 is <; 4 is >
        elif c2 == -1:
            c3 = compare(cn[0], cn[1])
            if c3 == 0:
                ret = (4, '>')
            elif c3 == 1:
                ret = (1, '<')
            elif c3 == -1:
                ret = (0, '<')
        
    return ret
            
def compare(l1, l2):
    global w
    w += 1
    
    return cmp(l1, l2)   
        
#     0  1  2  3| 4  5  6  7| 8  9  10 11  
cn = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

t_set = (
    ((0, '<'), (0, '>')),
    ((1, '<'), (1, '>')),
    ((2, '<'), (2, '>')),
    ((3, '<'), (3, '>')),
    ((4, '<'), (4, '>')),
    ((5, '<'), (5, '>')),
    ((6, '<'), (6, '>')),
    ((7, '<'), (7, '>')),
    ((8, '<'), (8, '>')),
    ((9, '<'), (9, '>')),
    ((10, '<'), (10, '>')),
    ((11, '<'), (11, '>')),    
)
fail = 0

for i in xrange(12):
    print 'Index:', i
    
    cn[i] = 0
    print cn
    r = find_anomalia(cn)
    print r
    
    if t_set[i][0] != r:
        fail += 1
        print 'Fail. Expect:', t_set[i][0], 'Got:', r
            
    cn[i] = 2
    print cn    
    r = find_anomalia(cn)
    print r
    
    if t_set[i][1] != r:
        fail += 1        
        print 'Fail. Expect:', t_set[i][1], 'Got:', r    
    
    cn[i] = 1
    print '-------------------'
    
print 'Fail number:', fail