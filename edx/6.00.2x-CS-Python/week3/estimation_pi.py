import random

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def throwNeedles(numNeedles):
    inCircle = 0
    for needle in xrange(numNeedles):
        x, y = random.random(), random.random()
        if (x * x + y * y) ** 0.5 <= 1:
            inCircle += 1
    return 4 * (inCircle / float(numNeedles))
    
def getEstimate(numNeedles, numTrials):
    estimates = []
    for trial in xrange(numTrials):
        estimates.append(throwNeedles(numNeedles))
    sDev = stdDev(estimates)
    curEst = sum(estimates) / len(estimates)
    print 'Estimate: ', curEst, ' stdDev: ', round(sDev, 6), ' Needles: ', numNeedles
    
    return (curEst, sDev)
    
def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision / 2.0:
        curEst, sDev = getEstimate(numNeedles, numTrials) 
        numNeedles *= 2
    return curEst
    
#estPi(0.005, 100)        