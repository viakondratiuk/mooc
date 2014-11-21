import random

def rollDie():
    return random.choice([1,2,3,4,5,6])
    
def rollUnfairDie():
    if random.random() < 1.0 / 5.5:
        return 6
    else:
        return random.choice([1,2,3,4,5])
    
def checkPascal(numTrials, roll):
    yes = 0.0
    for trial in xrange(numTrials):
        for r in xrange(24):
            die1 = roll()
            die2 = roll()
            if die1 == 6 and die2 == 6:
                yes += 1
                break
    print 'yes = ', yes, ', num_trials = ', numTrials, ', probability of loosing = ', 1.0 - yes / numTrials
    
#checkPascal(100000, rollDie)
#checkPascal(100000, rollUnfairDie)

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    success = 0.0
    for trial in range(numTrials):
        balls = [0,0,0,1,1,1]
        a = random.choice(balls)
        balls.remove(a)
        b = random.choice(balls)
        balls.remove(b)
        c = random.choice(balls)
        balls.remove(c)
        if a == b == c:
            success += 1
    return success / numTrials
    
print noReplacementSimulation(10000)