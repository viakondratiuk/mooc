import random, pylab

def roll_die():
    return random.choice([1,2,3,4,5,6])
    
def roll_coin():
    return random.choice([0,1])
    
def average(numTrials, func):
    sum = 0
    for i in xrange(numTrials):
        sum += func()
    return sum / float(numTrials)

def simulate_coin(numTrials):
    seq = []
    for i in xrange(numTrials):
        seq.append(roll_coin())
    return seq
    
def longest_streak(seq):
    cur = seq[0]
    cur_streak = streak = str(cur)
    for e in seq[1:]:
        if cur == e: 
            cur_streak += str(e)
        else: 
            cur_streak = str(e)
        cur = e
        if len(cur_streak) > len(streak): 
            streak = cur_streak
    return streak

#print average(100000, roll_die)
#seq = simulate_coin(100)
#print seq
#print longest_streak(seq)
#print average(100, roll_coin)

def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/float(numFlips)


def flipPlot(minExp, maxExp):
    """Assumes minExp and maxExp positive integers; minExp < maxExp
       Plots results of 2**minExp to 2**maxExp coin flips"""
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs)
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis, ratios)

##random.seed(0)
##flipPlot(4, 20)
##pylab.show()