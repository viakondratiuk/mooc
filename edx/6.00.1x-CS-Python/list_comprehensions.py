l = [x ** 2 for x in xrange(10)]
print l
l = [-1, -4, -9, -16]
l = [(i, i ** 2) for i in l]
print l
l = ['aaa ', '  bbb', 'cc']
l = [s.strip() for s in l]
print l
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

l = [i for row in matrix for i in row]
print l
l = [[row[i] for row in matrix] for i in range(4)]
print l

print zip(*matrix)