class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = float(value)
        self.weight = float(weight)
        
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value
        
    def getWeight(self):
        return self.weight
        
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
                 
def buildItems():
    # name, value, weight
    itemsTpl = (
        ('clock', 175, 10),
        ('painting', 90, 9),
        ('radio', 20, 4),
        ('vase', 50, 2),
        ('book', 10, 1),
        ('computer', 200, 20)
    )
    items = []
    for item in itemsTpl:
        items.append(Item(item[0], item[1], item[2]))
    return items
    

# Start greedy algorithms to build knapsack
def greedy(items, maxWeight, keyFcn):
    itemsCopy = sorted(items, key=keyFcn, reverse=True)
    print itemsCopy
    res = []
    totalVal = totalWeight = 0.0
    for item in itemsCopy:
        if item.getWeight() + totalWeight <= maxWeight:
            res.append(item)
            totalVal += item.getValue()
            totalWeight += item.getWeight()
    return (res, totalVal)
    
def value(item):
    return item.getValue()

def weightInverse(item):
    return -item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def testGreedy(items, constraint, getKey):
    taken, val = greedy(items, constraint, getKey)
    print('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

def testGreedys(maxWeight = 20):
    items = buildItems()
    print('Items to choose from:')
    for item in items:
        print '  ', item

    print 'Use greedy by value to fill a knapsack of size', maxWeight
    testGreedy(items, maxWeight, value)

    print 'Use greedy by weight to fill a knapsack of size', maxWeight
    testGreedy(items, maxWeight, weightInverse)

    print 'Use greedy by density to fill a knapsack of size', maxWeight
    testGreedy(items, maxWeight, density)
# End greedy algorithms to build knapsack    

# Start power set algorith to build knapsack
def choseBestSet(powerSet, constraint):
    bVal = 0.0
    bSet = None
    for s in powerSet:
        sVal = 0.0
        sWeight = 0.0
        for item in s:
            sVal += item.getValue()
            sWeight += item.getWeight()
        if sWeight <= constraint and sVal > bVal:
            bVal = sVal
            bSet = s
    return (bSet, bVal)
    
def genPowerSet01(items):
    powerSet = []
    itemsCount = len(items)
    psCount = 2 ** itemsCount

    for i in range(psCount):
        elem = []
        v = bin(i)[2:].zfill(itemsCount)
        for i in range(len(v)):
            if v[i] == '1':
                elem.append(items[i])
        powerSet.append(elem)
        
    return powerSet
    
def genPowerSetIterTools(items):
    from itertools import chain, combinations
    powerSet = []
    for i in chain.from_iterable(combinations(items, r) for r in range(len(items)+1)):
        powerSet.append(i)
    return powerSet
    
def genPowerSetSmart(items):
    powerSet = []
    N = len(items)
    for i in xrange(2 ** N):
        combo = []
        for j in xrange(N):
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        powerSet.append(combo)

    return powerSet
    
def genPowerSetRecursion(items):
    if not items:
        return [[]]
    return genPowerSetRecursion(items[1:]) + [[items[0]] + x for x in genPowerSetRecursion(items[1:])]

def printPowerSet(powerSet):
    for items in powerSet:
        for i in items:
            print i.getName(),
        print
        print '---'     
    
def testChoseBestSet():
    items = buildItems()
    #powerSet = genPowerSet01(items)
    #powerSet = genPowerSetIterTools(items)
    #powerSet = genPowerSetSmart(items)
    powerSet = genPowerSetRecursion(items)
    #printPowerSet(powerSet)
    taken, val = choseBestSet(powerSet, 20)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

testChoseBestSet()
# End power set algorith to build knapsack
                        
def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in one or zero bags.
    Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            if (i / 3**j) % 3 == 1: 
                bag1.append(items[j])
            elif (i / 3**j) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)                     
