class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None                
        
    def setLeftBranch(self, node):
        self.leftBranch = node
        
    def setRightBranch(self, node):
        self.rightBranch = node
        
    def setParent(self, parent):
        self.parent = parent
        
    def getValue(self):
        return self.value
    
    def getLeftBranch(self):
        return self.leftBranch
        
    def getRightBranch(self):
        return self.rightBranch
        
    def getParent(self):
        return self.parent
        
    def __str__(self):
        return str(self.value)        

def DFSBinary(root, fcn):
    stack = [root]
    seen = []
    while len(stack) > 0:
        print 'at node ' + str(stack[0].getValue())
        if fcn(stack[0]):            
            return True
        else:
            temp = stack.pop(0)
            seen.append(temp)
            if temp.getRightBranch() and not temp.getRightBranch() in seen:
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch() and not temp.getLeftBranch() in seen:
                stack.insert(0, temp.getLeftBranch())
                
    return False
    
def DFSBinaryPath(root, fcn):
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return tracePath(stack[0])
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
                
    return False
    
def DFSBinaryOrdered(root, fcn, ltFcn):
    stack = [root]
    while len(stack) > 0:
        print 'at node ' + str(stack[0].getValue())
        if fcn(stack[0]):            
            return True
        elif ltFcn(stack[0]):
            temp = stack.pop(0)
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())

                
    return False    

def BFSBinary(root, fcn):
    queue = [root]
    seen = []
    while len(queue) > 0:
        print 'at node ' + str(queue[0].getValue())
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            seen.append(temp)
            if temp.getLeftBranch() and not temp.getLeftBranch() in seen:
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch() and not temp.getRightBranch() in seen:
                queue.append(temp.getRightBranch())
                
    return False
    
def tracePath(node):
    if node.getParent():
        return [node] + tracePath(node.getParent())
    else:
        return [node]
                
def find6(node):
    return node.getValue() == 6

def lt6(node):
    return node.getValue() > 6    
            
def find3(node):
    return node.getValue() == 3    
    
def find10(node):
    return node.getValue() == 10
    
def lt10(node):
    return node.getValue() > 10
    
def buildDecisionTree(sofar, todo):
    if len(todo) == 0:
        return binaryTree(sofar)
    else:
        withElt = buildDecisionTree(sofar + [todo[0]], todo[1:])
        withoutElt = buildDecisionTree(sofar, todo[1:])
        here = binaryTree(sofar)
        here.setLeftBranch(withElt)
        here.setRightBranch(withoutElt)
        
        return here
        
def showBinaryTree(tree):
    if not tree.getLeftBranch():
        return 0
    if not tree.getRightBranch():
        return 0
    print str(tree.getLeftBranch()) + '--' + str(tree.getRightBranch())
    
    showBinaryTree(tree.getLeftBranch())
    showBinaryTree(tree.getRightBranch())
    
def DFSDTree(root, valueFcn, constraintFcn):
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(queue[0].getValue()):
            if best == None:
                best = queue[0]
                print best.getValue()
            elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                best = queue[0]
                print best.getValue()
            temp = queue.pop(0)
            if temp.getRightBranch():
                queue.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                queue.insert(0, temp.getLeftBranch())
        else:
            queue.pop(0)
    print 'visited', visited
    return best

def BFSDTree(root, valueFcn, constraintFcn):
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(queue[0].getValue()):
            if best == None:
                best = queue[0]
                print best.getValue()
            elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                best = queue[0]
                print best.getValue()
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
        else:
            queue.pop(0)
    print 'visited', visited
    return best
    
def sumValues(lst):
    vals = [e[0] for e in lst]
    return sum(vals)

def sumWeights(lst):
    wts = [e[1] for e in lst]
    return sum(wts)

def WeightsBelow10(lst):
    return sumWeights(lst) <= 10

def WeightsBelow6(lst):
    return sumWeights(lst) <= 6    
            
#print DFSBinary(n5, find6)
#print BFSBinary(n8, find6)
#print [e.getValue() for e in DFSBinaryPath(n5, find3)]
#print DFSBinaryOrdered(n5, find6, lt6)
#print DFSBinaryOrdered(n5, find10, lt10)

n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)
n10 = binaryTree(10)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n4.setRightBranch(n3)
n3.setParent(n4)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)

#Make this tree overgrown
n3.setLeftBranch(n5)
n5.setParent(n3)

#print DFSBinary(n5, find6)
#print BFSBinary(n5, find6)