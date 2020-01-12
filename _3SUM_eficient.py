x = [3, 1, 2, -5, -2, 10, 7, 3]
x.sort()
#print(x)
s = set()
for i in range(len(x)):
    a = i + 1
    b = len(x) - 1
    while a < b:
        suma = x[i] + x[a] + x[b]
        #print(x[i], x[a], x[b], suma)
        if(suma == 0):
            s.add((x[i], x[a], x[b]))
            a += 1
        elif(suma < 0):
            a += 1
        elif(suma > 0):
            b -= 1
print(s)
    