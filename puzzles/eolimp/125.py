h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())

t1 = 3600 * h1 + 60 * m1 + s1
t2 = 3600 * h2 + 60 * m2 + s2
t3 = t2 - t1
h3 = t3 // 3600
m3 = (t3 - 3600 * h3) // 60
s3 = t3 - 3600 * h3 - 60 * m3

print(h3, m3, s3)