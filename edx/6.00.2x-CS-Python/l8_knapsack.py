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
    
testGreedys()        