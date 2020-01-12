task = [(1, 6), (7, 11), (7, 9), (10, 12), (6, 8)]
task = sorted(task, key = lambda t:t[1])

print(task)

print(task[0])
fin, count = task[0][1], 1

for i in range(1, len(task)):

    if task[i][0] > fin:
        print(task[i])
        fin = task[i][1]
        count += 1
        
print(count)
