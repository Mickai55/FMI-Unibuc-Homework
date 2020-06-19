n = 3
m = 3

mat = [[1, 1, 4], 
       [1, 1, 2], 
       [1, 1, 1]]

mat2 = [row[:] for row in mat]

for i in range(n):
    list(mat[i])

for i in range(n):
    for j in range(m):
        if i == 0 and j != 0:
            mat[i][j] += mat[i][j - 1]
        elif j == 0 and i != 0:
            mat[i][j] += mat[i - 1][j]
        elif j != 0 and i != 0:
            mat[i][j] += max(mat[i - 1][j], mat[i][j - 1])

k = mat[i][j]
vectI = []
vectJ = []
u = []

while i != 0 or j != 0:
    if i == 0 and j == 1:
        u.append(mat2[0][1])
        vectI.append(0)
        vectJ.append(1)
        u.append(mat2[0][0])
        vectI.append(0)
        vectJ.append(0)
        break
    elif i == 1 and j == 0:
        u.append(mat2[1][0])
        vectI.append(1)
        vectJ.append(0)
        u.append(mat2[0][0])
        vectI.append(0)
        vectJ.append(0)
        break
    elif i == 0:
        u.append(mat2[i][j])
        vectI.append(i)
        vectJ.append(j)
        k = mat[i][j - 1]
        j -= 1
    elif j == 0:
        u.append(mat2[i][j])
        vectI.append(i)
        vectJ.append(j)
        k = mat[i - 1][j]
        i -= 1
    elif k - mat[i - 1][j] == mat2[i][j]:
        u.append(mat2[i][j])
        vectI.append(i)
        vectJ.append(j)
        k = mat[i - 1][j]
        i -= 1
    elif k - mat[i][j - 1] == mat2[i][j]:
        u.append(mat2[i][j])
        vectI.append(i)
        vectJ.append(j)
        k = mat[i][j - 1]
        j -= 1

vectI.reverse()
vectJ.reverse()

print(mat[n - 1][m - 1])

for i in range(len(vectI)):
    print (vectI[i] + 1, vectJ[i] + 1)


print(u)