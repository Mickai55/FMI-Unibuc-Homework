class Show:
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
    def __lt__(self, other):
         return self.y < other.y

n = 4
vect = []
vect.append(Show(1, 3, 1))
vect.append(Show(2, 6, 8))
vect.append(Show(4, 7, 2))
vect.append(Show(10, 11, 5))
profit = []
prev = []
maxval = 0
maxi = 0

vect.sort()

for i in range(n):
    profit.append(vect[i].w)
    prev.append(-1)

for i in range(1, n):
    for j in range(i):
        if vect[j].y <= vect[i].x:
            if profit[j] + vect[i].w > profit[i]:
                profit[i] = profit[j] + vect[i].w
                prev[i] = j
            if maxval < profit[i]:
                maxi = i
                maxval = profit[i]

i = maxi
size = 0
vect2 = []

while prev[i] != -1:
    vect2.append(vect[i])
    i = prev[i]
    size += 1
vect2.append(vect[i])
size += 1

sum = 0

for i in range(size - 1, -1, -1):
    sum += vect2[i].w

print(sum)

for i in range(size - 1, -1, -1):
    print(vect2[i].x, vect2[i].y)

print(profit)
print(prev)

for i in range(n):
    print(vect[i].x, vect[i].y, vect[i].w)