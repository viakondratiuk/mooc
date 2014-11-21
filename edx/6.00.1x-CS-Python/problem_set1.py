# -*- coding: utf-8 -*-

def longest_substring(s):
    c_start = 0
    r_start = 0
    r_end = 1
    
    for i in range(len(s)):
        if ((i + 1) - c_start) > (r_end - r_start):
            r_start = c_start
            r_end = i + 1
        if i+1 != len(s) and ord(s[i + 1]) < ord(s[i]):
            c_start = i + 1                      
    print ("Longest substring in alphabetical order is: " + s[r_start:r_end])
    
    return s[r_start:r_end]
    
def num_of_substr_occurs(s):
    count = 0
    for i in range(len(s)):
        if s[i:(i+3)] == 'bob':
            count += 1
    print('Number of times bob occurs is: ' + str(count))
    
    return count
    
# Test longest_substring
s = 'abcdefghijklmnopqrstuvwxyz'        
print longest_substring(s) == 'abcdefghijklmnopqrstuvwxyz'

s = 'qfukzfwtwowajafuud'        
print longest_substring(s) == 'afuu'

s = 'zyxwvutsrqponmlkjihgfedcba'        
print longest_substring(s) == 'z'

s = 'foiudutfrdvz'        
print longest_substring(s) == 'dvz'

s = 'blrfglkt'        
print longest_substring(s) == 'blr'

# Test num_of_substr_occurs
s = 'obfooboboebobbobobofobobo hobobobthehobowonder'
print num_of_substr_occurs(s) == 7

s = 'rkobooboobovbobobobobbbobbvtobssobobo'
print num_of_substr_occurs(s) == 6

s = 'obobbobobosbobobbobyjbobbbobobibobbiboz'
print num_of_substr_occurs(s) == 10