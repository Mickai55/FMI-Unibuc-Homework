x = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(x)
urm = [0] * n
best = [1] * n


for i in range(1, n):
    for j in range(i):
        if x[j] < x[i] and best[i] < best[j] + 1:
            best[i] = best[j] + 1
            urm[i] = j + 1

for i in range(n):
    if best[i] == max(best):
        ind = i

print(max(best))

for i in range(max(best)):
    print(x[ind], end = " ")
    ind = urm[ind] - 1

# x = [10, 22, 9, 33, 21, 50, 41, 60]
# n = len(x)

# mat = [[] for i in range(n)]

# for i in range(n - 1):
#     k = x[i]
#     mat[i].append(x[i])
#     for j in range(i, n):
#         if k < x[j]:
#             mat[i].append(x[j])
#             k = x[j]

# print(mat)