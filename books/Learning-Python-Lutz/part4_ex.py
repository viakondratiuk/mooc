def adder(a, b):
    return a + b
    
def adder2(*args):
    sum = args[0]
    for next in args[1:]:
        sum += next
    return sum
    
def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]
    return new
    
def addDict(d1, d2):
    union = {}
    for key in d1.keys():
        union[key] = d1[key]
    for key in d2.keys():
        union[key] = d2[key]
    return union
    
values = [1,2,4,9,16,25,36]
import math

res = []
for x in values: res.append(math.sqrt(x))
print res
print [math.sqrt(x) for x in values]
print map(math.sqrt, values)
print list((math.sqrt(x) for x in values))