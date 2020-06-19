cuvant1 = "jkjas"
cuvant2 = "antet"

m = len(cuvant1)
n = len(cuvant2)

d = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(m + 1):
    d[0][i] = i
for i in range(n + 1):
    d[i][0] = i

for j in range(1, m + 1):
    for i in range(1, n + 1):
        if cuvant1[i - 1] == cuvant2[j - 1]:
            diferenta = 0
        else:
            diferenta = 1
        aux = min(d[i - 1][j] + 1, d[i][j - 1] + 1)
        d[i][j] = min(aux, d[i - 1][j - 1] + diferenta)

for i in range(m + 1): 
    print(d[i])

k = n
l = m

while d[k - 1][l] != 0 and d[k][l - 1] != 0:
    if d[k - 1][l - 1] == d[k][l]:
        print("pastram", cuvant1[k - 1])
        k -= 1
        l -= 1
    else:
        aux = min(d[k - 1][l], d[k][l - 1])
        minim = min(aux, d[k - 1][l - 1])
        if minim == d[k - 1][l]:
            print("Stergem", cuvant1[k - 1])
            k -= 1
            l -= 1
        elif minim == d[k][l - 1]:
            print("A fost inserat caracterul:", cuvant2[l - 1])
            l -= 1
        elif minim == d[k - 1][l - 1]:
            print(l)
            print(cuvant1[k], "devine", cuvant2[l - 1])
            k -= 1
            l -= 1

print("Distanta Levenshtein este", d[n][m])
print(cuvant1)
print(cuvant2)

for i in range(m + 1): 
    print(d[i])