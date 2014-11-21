import random
import pylab

class Location(object):    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
        
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
        
    def distFrom(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y        
        return (xDist ** 2 + yDist ** 2) ** 0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
        
class Field(object):
    def __init__(self):
        self.drunks = {}
    
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLocation(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')

        return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return 'This drunk is named' + self.name
        
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.0),(0.0, -1.0),(1.0, 0.0),(-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,0.95), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
        
class PolarBear(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 0.5), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.5)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        deltaX = random.random()
        if random.random() < 0.5:
            deltaX = -deltaX
        deltaY = random.random()
        if random.random() < 0.5:
            deltaY = -deltaY
        return (deltaX, deltaY)        
                        
        
def walk(field, drunk, numSteps):
    start = field.getLocation(drunk)
    for step in xrange(numSteps):
        field.moveDrunk(drunk)
    
    return start.distFrom(field.getLocation(drunk))
    
def simWalks(numSteps, numTrials, drunk):
    homer = drunk('Homer')
    origin = Location(0, 0)
    distances = []
    for trial in xrange(numTrials):
        field = Field()
        field.addDrunk(homer, origin)
        distances.append(walk(field, homer, numSteps))
    return distances
    
def drunkTest(numTrials = 20):
    #random.seed(0)
    for numSteps in [10, 100, 1000, 10000]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print ' Mean =', sum(distances)/len(distances)
        print ' Max =', max(distances), 'Min =', min(distances)
        
def drunkTestPlot1(numTrials = 50):
    stepsTaken = [10, 50, 100, 500, 1000, 5000, 10000]
    meanDistances = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
    pylab.plot(stepsTaken, meanDistances, 'ro')
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()
    
def drunkTestPlot2(numTrials = 50):
    stepsTaken = [10, 50, 100, 500, 1000, 5000, 10000]
    meanDistances = []
    squareRootOfSteps = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
        squareRootOfSteps.append(numSteps**0.5)
    pylab.plot(stepsTaken, meanDistances, 'b-', label = 'Mean distance')
    pylab.plot(stepsTaken, squareRootOfSteps, 'g-.', label = 'Square root of steps')
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend()
    pylab.show()

def drunkTestPlot3(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    for dClass in (UsualDrunk, ColdDrunk, EDrunk):
        meanDistances = []
        for numSteps in stepsTaken:
            distances = simWalks(numSteps, numTrials, dClass)
            meanDistances.append(sum(distances)/len(distances))
        pylab.plot(stepsTaken, meanDistances, label = dClass.__name__)
        pylab.title('Mean Distance from Origin')
        pylab.xlabel('Steps Taken')
        pylab.ylabel('Steps from Origin')
        pylab.legend(loc = 'upper left')
    pylab.show()
    
drunkTestPlot3()