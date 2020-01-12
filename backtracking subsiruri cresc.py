v = [4, 2, 7, 9, 12, 10, 11, 15]
s = [None] * len(v)

def print_sol(count):
    print(s[0:count])

def lis(k, count):
    if (k == len(v)):
        print_sol(count)
    for i in range(k, len(v)):
        if v[i] > s[count - 1]:
            s[count] = v[i]
            lis(i+1, count + 1)

for i in range(len(v)):
    s[0] = v[i]
    lis(i+1, 1)