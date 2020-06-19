def suma():
    s = 0
    for q in range(n):
        s += mat[q][ind[q]]
    if s == k:
        for q in range(n):
            print(mat[q][ind[q]], end=" ")
        return s
    else:
        return 0

def recursion(p):
    for i in range(len(mat[p])):
        ind[p] = i
        if p == len(ind) - 1:
            if suma() != 0:
                exit(0)
        else:
            recursion(p + 1)


file = open("E:\Informatica\date.txt", "r")

n, k = file.readline().split()
n, k = int(n), int(k)
mat = [[] for i in range(n)]

for i in range(n):
    x = file.readline().split()
    mat[i] = [int(i) for i in x]
    mat[i].sort()

ind = [ 0 for i in range(len(mat)) ]

recursion(0)
