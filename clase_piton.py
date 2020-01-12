class Object:
    def __init__(self, id, cost, weight):
        self.id = id
        self.cost = cost
        self.weight = weight
    def __repr__(self):
        return "Obiectul " + str(self.id) + " are costul :" + str(self.cost) + " si greutatea " + str(self.weight) + "\n"

n, G = 4, 10
object = [None] * n
costs = [10, 9, 7, 5]
weights = [5, 4, 7, 3]

for i in range(n):
    object[i] = Object(i + 1, int(costs[i]), int(weights[i]))

object = sorted(object, key = lambda t:t.cost / t.weight, reverse = True)

print(object)

g, i, totalcost = 0, 0, 0

while i < n and g < G:
    if object[i].weight + g <= G:
        g += object[i].weight
        totalcost += object[i].cost
        print(object[i])
        i += 1
    else:
        costu = object[i].cost * (G - g) / object[i].weight
        print(Object(object[i].id, costu, G - g))
        totalcost += costu
        g = G

print(totalcost)
