from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()
        
class HTMLize:
    def write(self, line):
        print '<pre>%s</pre>' % line.rstrip()
        
if __name__ == '__main__':
    import sys
    obj = Uppercase(open('spam.txt'), sys.stdout)
    obj.process()
    obj1 = Uppercase(open('spam.txt'), open('spamup.txt', 'w'))
    obj1.process()
    Uppercase(open('spam.txt'), HTMLize()).process()    