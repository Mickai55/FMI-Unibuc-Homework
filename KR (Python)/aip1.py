n = int(input())
v = []

for i in range(n):
    v.append(int(input()))

v2 = v[:]

I = v.index(max(v))
print(v.pop(I))

I = v.index(max(v))
print(v.pop(I))

print(v, v2)