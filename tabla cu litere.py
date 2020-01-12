import queue

class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        

n = 4
m = 4
table = [
    ["A", "B", "C", "D"],
    ["E", "B", "C", "D"],
    ["F", "B", "X", "Z"],
    ["G", "H", "I", "D"],
]

used = [0 for i in range(92)] # 65 - A    91 - Z
dist = [0 for i in range(92)] # 65 - A    91 - Z
letters = [[] for j in range(92)]
q = queue.Queue()

used[ord(table[0][0])] = 1
q.put(Node(0, 0))
dist[ord(table[0][0])] = 0

letters[ord(table[0][0])].append(ord(table[0][0]))


while not q.empty():
    
    I, J = q.queue[0].i, q.queue[0].j

    # print(table[I][J], end=" ")

    # print(dist[ord(table[I][J])], end = " ")

    if I != n - 1 and not ord(table[I + 1][J]) in letters[ord(table[I][J])]:
        dist[ord(table[I + 1][J])] = dist[ord(table[I][J])] + 1
        q.put(Node(I + 1, J))
        letters[ord(table[I + 1][J])] = letters[ord(table[I][J])].copy()
        letters[ord(table[I + 1][J])].append(ord(table[I + 1][J]))
    
    if I != 0 and not ord(table[I - 1][J]) in letters[ord(table[I][J])]:
        dist[ord(table[I - 1][J])] = dist[ord(table[I][J])] + 1
        q.put(Node(I - 1, J))
        letters[ord(table[I - 1][J])] = letters[ord(table[I][J])].copy()
        letters[ord(table[I - 1][J])].append(ord(table[I - 1][J]))
        
    if J != m - 1 and not ord(table[I][J + 1]) in letters[ord(table[I][J])]:
        dist[ord(table[I][J + 1])] = dist[ord(table[I][J])] + 1
        q.put(Node(I, J + 1))
        letters[ord(table[I][J + 1])] = letters[ord(table[I][J])].copy()
        letters[ord(table[I][J + 1])].append(ord(table[I][J + 1]))
    
    if J != 0 and not ord(table[I][J - 1]) in letters[ord(table[I][J])]:
        dist[ord(table[I][J - 1])] = dist[ord(table[I][J])] + 1
        q.put(Node(I, J - 1))
        letters[ord(table[I][J - 1])] = letters[ord(table[I][J])].copy()
        letters[ord(table[I][J - 1])].append(ord(table[I][J - 1]))

    q.get()

Max = 0

# for i in range(65, 91):
#     print(chr(i), letters[i])

for i in range(65, 91):
    if len(letters[i]) > Max:
        Max = len(letters[i])
        car = i    

for i in range(len(letters[car])):
    print(chr(letters[car][i]), end=" ")

print()

print(chr(car), Max)
