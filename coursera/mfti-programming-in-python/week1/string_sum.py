import sys

digit_string = sys.argv[1]
print(sum(int(d) for d in digit_string))
