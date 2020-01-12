line = input().split()
p, n, m = int(line[0]), int(line[1]), int(line[2])
s, v = 0, [None] * p

line = input().split()
for i in range(p):
    v[i] = int(line[i])
v = sorted(v, reverse = True)

n, m = min(n ,m), max(n, m)
for i in range(n):
    s += v[i]/n

for i in range(n, n + m):
    s += v[i] / m
print(s)
