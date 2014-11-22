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
'''

def spiral_square(size):
    res = [size*[0] for i in range(size)]
    row = column = 0
    curSize = size
    count = 0
    for i in range(1, size*size):
        res[row][column] = i
        if i <= curSize:
            row += 1