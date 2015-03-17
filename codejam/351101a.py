def find_sum(_, items, p):
    f = open('out', 'a+')
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] + items[j] == c:
                f.write("Case #%d: %d %d\n" %(_ + 1, i + 1, j + 1))
    f.close()


lines = open('A-small-practice.in')
#lines = open('A-large-practice.in')

cases = int(lines.readline())
for _ in range(cases):
    c = int(lines.readline())
    i = int(lines.readline())
    items = map(int, list(lines.readline().split()))
    find_sum(_, items, c)