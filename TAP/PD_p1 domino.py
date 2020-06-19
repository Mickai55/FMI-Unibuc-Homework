class Domino: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def __repr__(self):
        return "(%s, %s)\n" % (self.x, self.y)
    def __lt__(self, other):
         return self.x < other.x

D = []
D.append(Domino(1, 2))
D.append(Domino(2, 3))
D.append(Domino(8, 3))
D.append(Domino(3, 4))
D.append(Domino(4, 9))
D.append(Domino(4, 5))
D.append(Domino(5, 6))

n = len(D)
lungimeMaximaLant = []
urmator = []

for i in range(n):
    lungimeMaximaLant.append(1)
    urmator.append(-1)

for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if D[i].y == D[j].x and lungimeMaximaLant[i] <= lungimeMaximaLant[j]:
            lungimeMaximaLant[i] = lungimeMaximaLant[j] + 1
            urmator[i] = j

Max = max(lungimeMaximaLant)

for j in range(n):
    if lungimeMaximaLant[j] == Max:
        i = j

while i != -1:
    print(D[i].x, D[i].y)
    i = urmator[i]

print(urmator)
print(lungimeMaximaLant)