class Adder:
    def __init__(self, data = []):
        self.data = data
    def add(self, x, y):
        print 'Not Implemented'
    def __add__(self, obj):
        return self.add(self.data, obj)
        
class ListAdder(Adder):
    def add(self, x, y):
        return x + y
        
class DictAdder(Adder):
    def add(self, x, y):
        d = dict(x)
        d.update(y)
        return d

#l = ListAdder([1,2,3])
#print l + [3,4,5]
#d = DictAdder({'a': 1, 'b': 2})
#print d + {'c': 3, 'd': 4}
'''        
a = Adder()
a.add(1, 2)
l = ListAdder()
print l.add([1,2,3], [3,4,5])
d = DictAdder()
print d.add({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
'''