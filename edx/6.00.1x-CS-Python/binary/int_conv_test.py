import int_conv

''' Tests '''
def test_general(testValues, t):
    flag = 0
   
    for k, v in testValues:
        b = int2bin(k, t)
        if b != v:
            print k, b, v
            flag += 1
            
    if flag == 0:
        print(t + ': OK')
    else:
        print(t + ' Error, ' + str(flag) + '/' + str(len(testValues)))
            
    return flag

def test_unsigned():
    testValues = [
        (0,   '00000000'),
        (1,   '00000001'),
        (7,   '00000111'),
        (127, '01111111'),
        (128, '10000000'),
        (255, '11111111'),
        (256, '00000000'),
        (512, '00000000'),
        (111, '01101111')
    ]
    test_general(testValues, 'us')
            
def test_sign_magnitude():
    testValues = [
        (0,    '10000000'),
        (-1,   '10000001'),
        (-7,   '10000111'),
        (-127, '11111111'),
        (-128, '10000000'),
        (-255, '11111111'),
        (-256, '10000000'),
        (-512, '10000000'),
        (-111, '11101111')
    ]
    test_general(testValues, 'sm')
        
def test_one_complement():
    testValues = [
        (0,    '11111111'),
        (-1,   '11111110'),
        (-7,   '11111000'),
        (-127, '10000000'),
        (-128, '11111111'),
        (-255, '10000000'),
        (-256, '11111111'),
        (-512, '11111111'),
        (-111, '10010000')
    ]
    test_general(testValues, '1c')
        
def test_two_complement():
    testValues = [
        (0,    '00000000'),
        (-1,   '11111111'),
        (-7,   '11111001'),
        (-127, '10000001'),
        (-128, '00000000'),
        (-255, '10000001'),
        (-256, '00000000'),
        (-512, '00000000'),
        (-111, '10010001')
    ]
    test_general(testValues, '2c')
        
def generate_bin_numbers():
    print('N Unsigned SignMagn 1Compl 2Compl')
    for x in (0, -1, -7, -127, -128, -255, -256, -512, -111):
        print x, int2bin(x, 'us'), int2bin(-x, 'sm'), int2bin(-x, 'oc'), int2bin(-x, 'tc')   

runTests1 = 0
if runTests1 == 1:
    print('Tests execution...')
    test_unsigned()
    test_sign_magnitude()
    test_one_complement()
    test_two_complement()
    print('Done!\n')

runTest2 = 0
if runTest2 == 1:
    a = int2bin(27, 'us')
    s = int2bin(-27, 'sm')
    c1 = int2bin(-27, '1c')
    c2 = int2bin(-27, '2c')
    
    print 'Sign Magnitude add: ', add_bin(a, s)
    print '1 Complement add: ', add_bin(a, c1)
    print '2 Complement add: ', add_bin(a, c2)