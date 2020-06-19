siruri = ["masa", "carte", "sac", "teatru", "tema", "rustic", "sare"]
n = len(siruri)
lungimeMaximaLant = []
urmator = []

for i in range(n):
    lungimeMaximaLant.append(1)
    urmator.append(-1)

for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if siruri[i][len(siruri[i]) - 2:] == siruri[j][:2] and lungimeMaximaLant[i] <= lungimeMaximaLant[j]:
            lungimeMaximaLant[i] = lungimeMaximaLant[j] + 1
            urmator[i] = j

Max = 1

for i in range(n):
    if lungimeMaximaLant[i] > Max:
        Max = lungimeMaximaLant[i]
        ind = i

i = ind

while i != -1:
    print(siruri[i])
    i = urmator[i]
