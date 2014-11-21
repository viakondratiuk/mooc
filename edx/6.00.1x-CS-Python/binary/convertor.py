'''
    d - direction to conver (dec2bin, bin2dec)
    n - number(18, -22.5, '111001') for convertion
    t - type of binary representation ('sm', '1c', '2c', 'fp', 'fl')
'''
def convert(d, n, t):
    assert t in ('sm', '1c', '2c', 'fp', 'fl'), 'Input conversion type is illegal'
    
    int_length = 8
           
    def to_binary(n, t):
        if type(n) == int:
            b = convert_decimal_part(n)            
            if t == 'sm':                
                b = to_sign_magnitude(b)
            elif t == '1c':
                b = to_one_complement(b)
            elif t == '2c':
                b = to_two_complement(b)
                
            return format_decimal(b)
        elif type(n) == float:
            l = split_float(n)
            s = get_sign(n)
            d = convert_decimal_part(l[0])
            f = convert_fractional_part(l[1])
            if t == 'fp':
                return s + '.' + ''.join(map(str, d)) + '.' + ''.join(f)

    # Integer to binary numbers convertion     
    def convert_decimal_part(n):
        n = abs(n)
        b = []
        while n > 0:
            b.insert(0, n % 2)
            n = n / 2
        
        return list_pad(b)
        
    def to_sign_magnitude(b):
        return [1] + b[1:]
        
    def to_one_complement(b):
        r = []
        for d in b:
            r.insert(0, 1 - d)
        return r
        
    def to_two_complement(b):
        # convert first number to 1 complement, pad the second number with 
        # leading zeros and sum them 
        return add_bin(to_one_complement(b), list_pad([1]))
        
    def add_bin(n1, n2):
        r = []
        carry = 0
        for b1, b2 in zip(reversed(n1), reversed(n2)):
            sum = carry
            sum += b1 + b2
            if sum >= 2:
                sum -= 2
                carry = 1
            else:
                carry = 0
            r.insert(0, sum)
        
        return r

    # Fractional to binary numbers convertion
    def convert_fractional_part(n):
        p = 1
        while (n * (2 ** p)) % 1 != 0:
            p += 1              
        num = int((2 ** p) * n)
        
        r = []
        if num == 0:
            r = ['0']
        while num > 0:
            r.insert(0, str(num % 2))
            num = num / 2
    
        for i in range(p - len(r)):
            r.insert(0, '0')
            
        return r
        
    # General functions                
    def get_sign(n):
        if n < 0:
            return '1'
        return '0'        
        
    def split_float(n):
        l = str(n).split('.')
        l[0] = int(l[0])
        l[1] = float('0.' + l[1])
        return l
    
    def list_pad(l):
        s = int_length
        for i in range(s - len(l)):
            l.insert(0, 0)
        return l
        
    def format_decimal(b):
        return ''.join(map(str, b)).zfill(int_length)
        
    # Convert binary number to decimal
    def to_decimal(n, t):
        if t == 'int':
            decimal = 0
            exp = 0
            
            for bit in n[::-1]:
                decimal += 2 ** exp * int(bit)
                exp += 1
            return decimal
        elif t == 'fp':            
            result = to_decimal(n[1:4], 'int')
            exp = 1
            fp = 0.0
            for bit in n[4:9]:
                fp += 0.5 ** exp * int(bit)
                exp += 1
            result = float(result) + fp
            sign = (n[0] == '1') and '-' or ''
            
            return sign + str(result)
                
    # Start of convertion
    if d == 'dec2bin':
        assert type(n) in (int, float), 'Input number type is illegal'
        return to_binary(n , t)
    elif d == 'bin2dec':
        assert type(n) == str, 'Input number type is illegal'
        return to_decimal(n, t)
    
#print convert('dec2bin', -10, 'sm')
#print convert('dec2bin', -10, '1c')
#print convert('dec2bin', -10, '2c')
#print convert('dec2bin', -1.5625, 'fp')
#print convert('bin2dec', '111', 'sm')
#print convert('bin2dec', '101', 'sm')
#print convert('bin2dec', '110', 'sm')
#print convert('bin2dec', '1110', 'sm')
for i in range(255, 127, -1):
    b = '{0:08b}'.format(i)
    print (127 - i), ':', convert('bin2dec', b, 'fp') 

for i in range(0, 128):
    b = '{0:08b}'.format(i)
    print i, ':', convert('bin2dec', b, 'fp')   


'''
1.  | Real number to normal scientific form
1.5 | 1.0001 * 2^10, where we can skip leading 1
2.  | 1 bit - sign, 2,3,4 - exponent, 5,6,7,8 - significand
3.  | exponent couldn't be negative, so we should apply bias, for 8 bits add the bias: 2^(exp bits - 1) - 1 = 2^(3-1)-1 = 4-1 = 3
4.  | 0.1 -> 1.0 * 2^-1 -> 0 ___ 0000

Algorithm dec2float:
    1. Number: 0.5625
    2. To Binary: 0.1001
    3. Normalize: 1.001 * 2^(-1)
    4. Add bias to exponent: -1 + 3 = 2
    5. Biased to bin
    
Algorithm float2dec:
    0. sign * 1.significand * 2 ** exponent
    1. 0 010 0010
    2. Sign bit 
    3. Saved exponent - 3
    4. (-1)^0 * 1.0010 * 2^(-1)
    
0 111 0000 : +inf
1 111 0000 : -inf

0 111 0100 (non zero): NaN

Largest real number: 0 110 1111 = 15.5

Denormalized case
0 000 0000 = (-1)^0 * (1.0000)*2^(0-3) = 0.125 - wrong
if exp bits are all 0 we denormalize number
0 000 0000 = (-1)^0 * (0.0000)*2^(0-3) = 0 - wrong
exp : 1 - bias
'''