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
'''

def spiral_square(size):
    res = [size*[0] for i in range(size)]
    row = column = 0
    for i in range(1, size*size):
        res[row][column] = i