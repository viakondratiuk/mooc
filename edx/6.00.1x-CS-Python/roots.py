# Functions to find roots!
def sqrt_average(x, epsilon):
    numOfGuesses = 1
    answer = x / 2.0
    
    while abs(answer ** 2 - x) > epsilon:
        numOfGuesses += 1
        answer = (answer + x / answer) / 2
    print('NumOfGusses by averaging is: ' + str(numOfGuesses))
    
    return answer

def approx_root(x, power, epsilon):
    step = epsilon ** 2
    numOfGuesses = 1
    answer = 0
    
    while abs(x - answer ** power) >= epsilon and answer <= x:
        answer += step
        numOfGuesses += 1
    print('NumOfGusses by approximation method is: ' + str(numOfGuesses))
    
    return answer
    
def bisect_root(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None
    
    numOfGuesses = 1
    lo = min(-1, x)
    hi = max(1, x)    
    answer = (hi + lo) / 2.0
    
    while abs(answer ** power - x) > epsilon:        
        numOfGuesses += 1
        if answer ** power < x:
            lo = answer
        else:
            hi = answer
        answer = (hi + lo) / 2.0
    print('NumOfGusses by bisection search is: ' + str(numOfGuesses))
    
    return answer
    
def sqrt_newthon_raphson(x, epsilon):
    answer = x / 2.0
    numOfGuesses = 1
    
    while abs(x - answer ** 2) >= epsilon:
        numOfGuesses += 1
        answer = answer - (answer ** 2 - x) / (2 * answer)
    print('NumOfGusses by Newthon-Raphson method is: ' + str(numOfGuesses))
    
    return answer

# Tests of functions for finding roots
def test_sqrt_average():
    for x in (4, 9, 16, 25, 36, 49, 64):
        res = sqrt_average(x, 0.01)
        print("Sqrt(" + str(x) + ") ~= " + str(res))

def test_approx_root():
    for x in (4, 9, 16, 25, 36, 64):
        for power in (1, 2, 3):
            res = approx_root(x, power, 0.01)
            print("  " + str(x) + " root " + str(power) + " ~= " + str(res))
    
    
def test_bisect_root():
    for x in (0.25, -0.25, 2, -2, 4, -4, 8, -8):
        for power in range(1, 4):
            res = bisect_root(x, power, 0.001)
            if res == None:
                print("  No root of " + str(x))
            else:
                print("  " + str(x) + " root " + str(power) + " ~= " + str(res))

def test_sqrt_newthon_raphson():
    for x in (2, 4, 8, 16, 25, 36, 128):
        res = sqrt_newthon_raphson(x, 0.01)
        print("Sqrt(" + str(x) + ") ~= " + str(res))

# Section for test functions
#test_sqrt_average()
#test_approx_root()
#test_bisect_root()
#test_sqrt_newthon_raphson()

# Section to compare number of guesses of different root methods
root = 225
epsilon = 0.01
power = 2

sqrt_average(root, epsilon)
approx_root(root, power, epsilon)
bisect_root(root, power, epsilon)
sqrt_newthon_raphson(root, epsilon)

# sqrt_average and sqrt_newthon_raphson have the same formulas at the result ((a ** 2 - x)/2 * a)