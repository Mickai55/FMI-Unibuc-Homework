import bisect

x = [11, 13, 10, 15, 12, 7]
n = len(x)

mat = [[x[0]]]
i = 1
V = [x[0]]
for i in range(1, len(x)):
    l  = bisect.bisect_left(V, x[i], 0)
    if l < len(mat) and len(mat[l]):
        mat[l].append(x[i])
        V[l] = x[i]
    else:
        mat.append([x[i]])
        V.append(x[i]) 
for line in mat:
    print(line)

