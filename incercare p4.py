# 3 11
# 3 5 10 8
# 4 3 7
# 6 8 2 9

file = open("E:\Informatica\date.txt", "r")

n, k = file.readline().split()
n, k = int(n), int(k)
mat = [[] for i in range(n)]

for i in range(n):
    x = file.readline().split()
    mat[i] = [int(i) for i in x]
    # mat[i].sort()

sume = [ [0 for i in range(k + 1)] for j in range(n)]

for i in range(len(mat[0])):
    sume[0][mat[0][i]] = i + 1

for i in range(1, n):
    for u in range(1, k + 1):
        if sume[i - 1][u] != 0:
            for j in range(len(mat[i])):
                p = u + mat[i][j]
                if p <= k:
                    sume[i][p] = j + 1

q = sume[n - 1][k]
w = mat[n - 1][q - 1]
print(w)

for i in range(n - 2, -1, -1):
    k = k - w
    q = sume[i][k]
    w = mat[i][q - 1]
    print(w)

