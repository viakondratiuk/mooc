def caesar_helper(shift, t):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    word = raw_input('Enter your input: ').lower()
    result = ''

    for letter in word:
        if letter in alph:
            if t == 'crypt':
                index = (alph.find(letter) + shift) % 26
            elif t == 'decrypt':
                index = (alph.find(letter) - shift) % 26
            result += alph[index]
        else:
            result += letter

    return result

def caesar_crypt(shift):
    return caesar_helper(shift, 'crypt')
    
def caesar_decrypt(shift):
    return caesar_helper(shift, 'decrypt') 
    
def rot13():
    return caesar_helper(13, 'crypt')