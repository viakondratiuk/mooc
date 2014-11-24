'''
Function to create spiral squares.
Input: square size
Output: spiral square
print spiral_square(4)
[
[1, 2, 3, 4],
[12, 13, 14, 5],
[11, 16, 15, 6],
[10, 8, 9, 7],
]
----
The way how we should fill cells with numbers:
row = 0, column = 0-3
(0, 0), (0, 1), (0, 2), (0, 3),

row = 1-3, column = 3
(1, 3), (2, 3), (3, 3),

row = 3, column = 2-0
(3, 2), (3, 1), (3, 0),

row = 2-1, column = 0
(2, 0), (1, 0),

row = 1, column = 1-2
(1, 1), (1, 2),

row = 2, column = 2
(2, 2),

row = 2, column = 1
(2, 1)
Read:
    http://codegolf.stackexchange.com/questions/769/print-nxn-spiral-of-ascending-numbers
    http://rosettacode.org/wiki/Spiral_matrix#Python
'''

def spiral_square(size):
    res = [size*[0] for i in range(size)]
    row = column = 0
    cycle, steps, curStep = 1, size, 0
    
    for i in range(1, size*size + 1):        
        res[row][column] = format(i, '02')
        curStep +=1
        #print 'pos='+str(row)+':'+str(column),'i=',i,'steps=',steps,'curStep=',curStep,'cycle=',cycle
        
        if cycle == 1:
            if steps == curStep:
                cycle, steps, curStep = 2, steps - 1, 0                
            else:
                column += 1            
            
        if cycle == 2:
            if steps == curStep:
                cycle, curStep = 3, 0
            else:
                row += 1
                
        if cycle == 3:
            if steps == curStep:
                cycle, steps, curStep = 4, steps - 1, 0
            else:
                column -= 1
                            
        if cycle == 4:
            if steps == curStep:
                cycle, curStep, column = 1, 0, column + 1
            else:
                row -= 1                
    return res
    
size = 3
for row in spiral_square(size):
    print row