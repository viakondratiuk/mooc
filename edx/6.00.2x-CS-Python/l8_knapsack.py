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
    items = (
        ('clock', 175, 10),
        ('painting', 90, 9),
        ('radio', 20, 4),
        ('vase', 50, 2),
        ('book', 10, 1),
        ('computer', 200, 20)
    )
    itemsObjs = []
    for i in items:
        itemsObjs.append(Item(i[0], i[1], i[2]))
    return itemsObjs
    
def greedy(items, maxWeight, keyFcn):
    itemsCopy = sorted(items, key=keyFcn, reverse = True)
    res = []
    totalVal = totalWeight = 0.0
    for i in itemsCopy:
        if totalWeight > maxWeight: break
        if i.getWeight() + totalWeight <= maxWeight:
            res.append(i)
            totalVal += i.getValue()
            totalWeight += i.getWeight()
    return (res, totalVal)
    
def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def testGreedy(Items, constraint, getKey):
    taken, val = greedy(Items, constraint, getKey)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

def testGreedys(maxWeight = 20):
    Items = buildItems()
    print('Items to choose from:')
    for item in Items:
        print '  ', item
    print 'Use greedy by value to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, value)
    print 'Use greedy by weight to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, weightInverse)
    print 'Use greedy by density to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, density)
    
        