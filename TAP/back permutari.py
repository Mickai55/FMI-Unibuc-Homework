def cont(k):
    for i in range(k):
        for j in range(i + 1, k + 1):
            if x[i] == x[j]:
                return 0
    return 1

def back(k):
    for i in range(n):
        x[k] = i
        
        if k == n - 1:
            # if cont(k):
            print(x)
        else:
            back(k + 1)

n = 3
x = [0 for i in range(n)]

back(0)