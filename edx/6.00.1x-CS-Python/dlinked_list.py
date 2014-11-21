class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
        
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
        
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
        
    def getBefore(self):
        return self.before
        
    def getAfter(self):
        return self.after
        
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    def insert_after(atMe, newFrob):
        temp = atMe.getAfter()
        atMe.setAfter(newFrob)
        newFrob.setBefore(atMe)
        newFrob.setAfter(temp)
        temp.setBefore(newFrob)
        
    def insert_before(atMe, newFrob):
        temp = atMe.getBefore()
        atMe.setBefore(newFrob)
        newFrob.setAfter(atMe)
        newFrob.setBefore(temp)
        temp.setAfter(newFrob)
        
    if atMe.myName() < newFrob.myName():
        if atMe.getAfter() is None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif atMe.getAfter().myName() > newFrob.myName():                
            insert_after(atMe, newFrob)
        else:
            insert(atMe.getAfter(), newFrob)
    elif atMe.myName() > newFrob.myName():        
        if atMe.getBefore() is None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif atMe.getBefore().myName() < newFrob.myName():
            insert_before(atMe, newFrob)  
        else:
            insert(atMe.getBefore(), newFrob)
    elif atMe.myName() == newFrob.myName():
        temp = atMe.getBefore()
        if temp is not None:
            temp.setAfter(newFrob)
        atMe.setBefore(newFrob)
        newFrob.setBefore(temp)
        newFrob.setAfter(atMe)

        
def printForward(e):
    print "Forward:"
    c = e
    while c is not None:
        print c.myName()
        c = c.getAfter()
        
def printBackward(e):    
    print "Backward:"
    c = e
    while c is not None:
        print c.myName()
        c = c.getBefore()
        
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore() == None:
        return start
    return findFront(start.getBefore())        
        
'''
l = Frob('leonid')
a = Frob('amara')
j1 = Frob('jennifer')
j2 = Frob('jennifer')
s = Frob('scott')

insert(l, s)
insert(s, j1)
insert(s, j2)
insert(j1, a)
'''
e1 = Frob('eric')
e2 = Frob('eric')
e3 = Frob('eric')
c1 = Frob('chris')
c2 = Frob('chris')
c3 = Frob('chris')
j1 = Frob('john')
j2 = Frob('john')
j3 = Frob('john')

insert(e1, e2)
insert(e1, c1)
insert(e1, j1)
insert(e1, j2)
insert(e1, c2)
insert(e1, e3)
insert(e1, j3)
insert(e1, c3)

printForward(c2)
print '-----------------------------'
#printForward(c2)
#print '-----------------------------'
#printForward(c3)
#print '-----------------------------'
printBackward(j1)
'''
print '-----------------------------'
print j2.getBefore().myName()
print j2.myName()
print j2.getAfter()
print '-----------------------------'
print j1.getBefore().myName()
print j1.myName()
print j1.getAfter()
'''
'''
andrew = Frob('andrew')
eric = Frob('eric')
fred = Frob('fred')
martha = Frob('martha')
ruth = Frob('ruth')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

print 'Andrew'
print 'before: ', andrew.getBefore()
print 'name: ', andrew.myName()   
print 'after: ', andrew.getAfter().myName()
print '-----------------------------'

print 'Eric'
print 'before: ', eric.getBefore().myName()
print 'name: ', eric.myName()   
print 'after: ', eric.getAfter().myName()
print '-----------------------------'

print 'Fred'
print 'before: ', fred.getBefore().myName()
print 'name: ', fred.myName()   
print 'after: ', fred.getAfter().myName()
print '-----------------------------'

print 'Martha'
print 'before: ', martha.getBefore().myName()
print 'name: ', martha.myName()   
print 'after: ', martha.getAfter().myName()
print '-----------------------------'

print 'Ruth'
print 'before: ', ruth.getBefore().myName()
print 'name: ', ruth.myName()   
print 'after: ', ruth.getAfter()
print '-----------------------------'
'''