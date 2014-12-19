import random
import pylab

# Global Variables
MAXRABBITPOP = 100
CURRENTRABBITPOP = 10
CURRENTFOXPOP = 20

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    pRabbitRepr = 1.0 - CURRENTRABBITPOP / float(MAXRABBITPOP)
    for i in xrange(CURRENTRABBITPOP):
        if random.random() < pRabbitRepr:
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP    
    
    pFoxEatRabbit = CURRENTRABBITPOP / float(MAXRABBITPOP)
    for i in xrange(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10 and random.random() < pFoxEatRabbit:
            CURRENTRABBITPOP -= 1
            if random.random() < 1/float(3):
                CURRENTFOXPOP += 1
        else:
            if CURRENTFOXPOP > 10 and random.random() < 1/float(10):
                CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rPop = []
    fPop = []
    for i in xrange(numSteps):
        rabbitGrowth()
        foxGrowth()
        rPop.append(CURRENTRABBITPOP)
        fPop.append(CURRENTFOXPOP)        
    return (rPop, fPop)
    
print runSimulation(100)