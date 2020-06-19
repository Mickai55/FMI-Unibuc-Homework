v = [6, 3, 5, 10 , 12, 2, 9, 15, 14, 7, 4, 8, 13]
n = len(v)
L = [1] * len(v)
succ = [n] * len(v)
L[n-1] = 1
poz_max = n - 1
for i in range(n-2, -1, -1):
    for j in range(i + 1, n):
        if v[i] < v[j] and L[j] + 1 > L[i]:
            L[i] = L[j] + 1
            succ[i] = j
        if L[i] > L[poz_max]:
            poz_max = i

k = poz_max
while k < n:
    print(v[k])
    k = succ[k]