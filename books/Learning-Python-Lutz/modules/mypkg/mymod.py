def countLines(*files):
    countLine = 0
    for path in files:
        f = open(path)
        countLine += len(f.readlines())
    return countLine
    
def countChars(*files):
    countChar = 0
    for path in files:
        with open(path) as f:
            for line in f:
                countChar += len(line)
    return countChar    
                
def test():
    f = 'reloadall.py'    
    print countLines(f)
    print countChars(f)
    print 'you will never catch me!'
    
    
if __name__ == '__main__':
    test()    