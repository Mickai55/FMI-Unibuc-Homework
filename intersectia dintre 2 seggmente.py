import math

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

def lineFromPoints(P, Q): 
    a = P.y - Q.y
    b = Q.x - P.x  
    c = P.x * Q.y - Q.x * P.y
    return a, b, c

def distance(P, Q):
    return math.sqrt((P.x - Q.x) * (P.x - Q.x) + (P.y - Q.y) * (P.y - Q.y))

A = []

A.append(Point(0, 4))
A.append(Point(4, 4))
A.append(Point(0, 0))
A.append(Point(4, 0))

# A.append(Point(0, 0))
# A.append(Point(2, 2))
# A.append(Point(0, 3))
# A.append(Point(3, 0))

a1, b1, c1 = lineFromPoints(A[0], A[1])
a2, b2, c2 = lineFromPoints(A[2], A[3])

delta = a1 * b2 - b1 * a2

if delta:
    print("Nu sunt coliniare!")
    x = ((-c1 * b2) - (b1 * -c2)) / delta
    y = ((a1 * -c2) - (-c1 * a2)) / delta

    if x < max(A[0].x, A[1].x) and x > min(A[0].x, A[1].x) and y < max(A[0].y, A[1].y) and y > min(A[0].y, A[1].y):
        if x < max(A[2].x, A[3].x) and x > min(A[2].x, A[3].x) and y < max(A[2].y, A[3].y) and y > min(A[2].y, A[3].y):
            print("Segmentele se intersecteaza in punctul: (", x, ",", y, ")")
        else:
            print("Nu se intersecteaza.")
    else:
            print("Nu se intersecteaza.")
elif c1 == c2:
    print("Sunt coliniare!")
    k = max(A[0].x, A[1].x, A[2].x, A[3].x)
    q = min(A[0].x, A[1].x, A[2].x, A[3].x)

    x_left = -1
    x_right = -1

    for i in range(q, k):
        if (i >= min(A[0].x, A[1].x) and i <= max(A[0].x, A[1].x)) and (i >= min(A[2].x, A[3].x) and i <= max(A[2].x, A[3].x)):
            x_left = i
            break
    for i in range(k, q, -1):
        if (i >= min(A[0].x, A[1].x) and i <= max(A[0].x, A[1].x)) and (i >= min(A[2].x, A[3].x) and i <= max(A[2].x, A[3].x)):
            x_right = i
            break
    if x_left != -1 and x_right != -1:
        y_left = (-c1 - a1 * x_left) // b1
        y_right = (-c1 - a1 * x_right) // b1

        if x_left != x_right:
            print("Se intersecteaza in segmentul dintre punctele: (", x_left, ",", y_left, ") si (", x_right, ", ", y_right, ").")
        else:
            print("Se intersecteaza in punctul: (", x_left, ",", y_left, ")")
    else:
        print("nu se int")
else:
    print("Sunt parelele.")