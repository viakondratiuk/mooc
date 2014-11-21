import random

def roll_die():
    return random.choice([1,2,3,4,6])
    
def roll_n(n):
    result = ''
    for i in xrange(n):
        result += str(roll_die())
    return result
    
def get_target(goal):
        numTries = 0
        numRolls = len(goal)
        while True:
            numTries += 1
            result = roll_n(numRolls)
            if result == goal:
                return numTries
                
def run_simulation(goal, numTrials):
    total = 0
    for i in xrange(numTrials):
        total += get_target(goal)
    return total / float(numTrials)
    
#print 'Average number of tries = ' + str(run_simulation('11111', 100))
#print 'Average number of tries = ' + str(run_simulation('46466', 100))

def at_least_one_one(numRolls, numTrials):
    numSuccess = 0
    for i in range(numTrials):
        rolls = roll_n(numRolls)
        if '1' in rolls:
            numSuccess += 1
        fracSuccess = numSuccess / float(numTrials)
    return fracSuccess

print at_least_one_one(10, 1000)