n = 10
s = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            for u in range(n):
                s = s + i + j + k
print(s)