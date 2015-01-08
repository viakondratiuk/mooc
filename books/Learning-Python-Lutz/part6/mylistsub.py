from mylist import MyList

class MyListSub(MyList):
    calls = 0
    def __init__(self, start):
        self.adds = 0
        MyList.__init__(self, start)
    def __add__(self, other):
        print 'add:',str(other)
        MyListSub.calls += 1
        self.adds += 1
        return MyList.__add__(self, other)
    def stats(self):
        return self.calls, self.adds
        
if __name__ == '__main__':
    x = MyListSub('spam')
    y = MyListSub('foo')
    print x[2]
    print x[1:]
    print x + ['ab']
    print x + ['bc']
    print y + ['mm']
    print x.stats()
    print y.stats()