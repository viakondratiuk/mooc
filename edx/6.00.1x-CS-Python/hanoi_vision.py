def hanoi_vision(n, from1, temp, to, caller='start'):
    print (3-n)*"| " + str(n), caller, (from1, temp, to)
    if n > 0:
        hanoi_vision(n - 1, from1, to, temp, 'func1')
        print (3-n)*"| " + str(n), '-- Move disc from {} to {}'.format(from1, to)
        hanoi_vision(n - 1, temp, from1, to, 'func2')
    else:
        print (3-n)*"| " + str(n), 'n = 0, return'

hanoi_vision(3, 'A', 'B', 'C')

'''
1. func1: move (n-1) disk on temp pin
2. move n disk on target pin
3. func2: move (n-1) disk on target pin
'''