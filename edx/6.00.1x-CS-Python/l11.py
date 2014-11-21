class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y
        
    def __repr__(self):
        return "Coordinate(%d, %d)" % (self.x, self.y)
        

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
            
    def intersect(self, obj):
        result = intSet()
        for item in obj.vals:
            if self.member(item):
                result.insert(item)
                
        return result
        
    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def __len__(self):
        return len(self.vals)

class Queue(object):
    def __init__(self):
        ''' Creates an empty set for queue '''
        self.vals = []
        
    def insert(self, e):
        ''' Inserts an element into queue beginning '''
        self.vals.append(e)
        
    def remove(self):
        try:
            print self.vals.pop(0)
        except:
            raise ValueError('The queue is empty')

q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
q.remove()
'''
# tests for int sets
a = intSet()
b = intSet()

a.insert(1)
a.insert(2)
a.insert(3)

b.insert(2)
b.insert(3)
b.insert(4)

c = a.intersect(b)
print c
print len(c)

# tests for coordinates
a = Coordinate(2, 10)
b = Coordinate(12, 14)
c = Coordinate(2, 10)

print a
print b
print c

print a == b
print a == c

print repr(a)
print repr(b)

m = eval(repr(a))
print m
print m == c
'''