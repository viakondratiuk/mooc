import sys

num_steps = int(sys.argv[1])

for i in range(num_steps):
    space = (num_steps - (i + 1)) * " "
    hashtag = (i + 1) * "#"
    print(space + hashtag)
