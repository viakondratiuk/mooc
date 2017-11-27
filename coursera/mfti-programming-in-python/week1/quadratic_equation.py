import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)

print(int(x1))
print(int(x2))
