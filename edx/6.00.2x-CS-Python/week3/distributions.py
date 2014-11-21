import random, pylab

def normal(mean, stdDev, numSamples):
    samples = []
    for sample in xrange(numSamples):
        samples.append(random.gauss(mean, stdDev))
    pylab.hist(samples, bins = 101)
    pylab.show()    

def expNotMonteCalo(n, clearProb, steps):
    numRemaining = [n]
    for step in xrange(steps):
        numRemaining.append(n*((1-clearProb)**step))
        pylab.plot(numRemaining, label = 'Exponential Decay')
        
def expMonteCalo(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numLeft = numRemaining[-1]
        for m in range(numRemaining[-1]):
            if random.random() <= clearProb: 
                numLeft -= 1
        numRemaining.append(numLeft)
    pylab.plot(numRemaining, 'ro', label = 'Simulation')
    
expNotMonteCalo(10000, 0.01, 1000)
#expMonteCalo(10000, 0.01, 1000)
pylab.xlabel('Number of Steps')
pylab.ylabel('Number of Molecules')
pylab.show()