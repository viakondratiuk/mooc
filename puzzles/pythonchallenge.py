def pzl3():
    s = """sldfslfsdjfnjh"""
    #print s[0:3] + '-' + s[3:4] + '-' + s[4:7]
    l = r = m = 0
    r = ''
    for i in xrange(9, len(s)):
        if (
            s[i+1:i+8].isalpha() and 
            not s[i:i+1].isupper() and 
            s[i+1:i+4].isupper() and 
            s[i+4:i+5].islower() and
            s[i+5:i+8].isupper() and
            not s[i+8:i+9].isupper()
           ): 
            print s[i+4]
    return r
        
print pzl3()
