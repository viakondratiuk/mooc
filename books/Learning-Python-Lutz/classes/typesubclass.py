class MyList(list):
    def __getitem__(self, offset):
        print ('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)
        
class Set(list):
    def __init__(self, value = []):
        list.__init__([])
        self.concat(value)

    def intersect(self, other):
        return Set([i for i in self if i in other])
        
    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res
        
    def concat(self, value):
        for i in value:
            if i not in self:
                self.append(i)
                
    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return 'Set:' + list.__repr__(self)
        
        
if __name__ == '__main__':
    print list('abc')
    x = MyList('abc')
    print x
    print x[1]
    print x[2]
    
    x.append('spam'); print x;
    x.reverse(); print x;
    
    a = Set([1,3,5,7])
    b = Set([2,1,4,5,6])
    print a, b, len(a), len(b)
    print a.intersect(b), b.union(a)
    print a & b, b | a