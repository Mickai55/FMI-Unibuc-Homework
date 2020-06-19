class Point: 
    def __init__(self, x, y, roll): 
        self.x = x 
        self.y = y 
        self.roll = roll
    def __lt__(self, other):
         return self.x < other.x

def aria(p1, p2, p3): 
    return abs((p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)) / 2 )

def inauntru(p1, p2, p3, punct): 
    A = aria (p1, p2, p3) 
    A1 = aria (punct, p2, p3) 
    A2 = aria (p1, punct, p3) 
    A3 = aria (p1, p2, punct) 
      
    if(A == A1 + A2 + A3): 
        return True
    else: 
        return False

def lineFromPoints(P, Q): 
  
    a = Q.y - P.y
    b = P.x - Q.x  
    c = a*(P.x) + b*(P.y)  
    return a, b, c
  

points = []
points.append(Point(0, 0, 1))
points.append(Point(0, 5, 2))
points.append(Point(5, 5, 3))
points.append(Point(1, 1, 4))

if aria(points[0], points[1], points[2]) == 0 and aria(points[1], points[2], points[3]) == 0:
    points.sort()
    print("SEGEMENT")
    print("I = {", points[0].roll, points[3].roll, "}")
    print("J = {", points[1].roll, points[2].roll, "}")

elif inauntru(points[0], points[1], points[2], points[3]):
    print("TRIUNGHI")
    print("I = {", points[0].roll, points[1].roll, points[2].roll, "}")
    print("J = {", points[3].roll, "}")

elif inauntru(points[1], points[2], points[3], points[0]):
    print("TRIUNGHI")
    print("I = {", points[1].roll, points[2].roll, points[3].roll, "}")
    print("J = {", points[0].roll, "}")

elif inauntru(points[2], points[3], points[0], points[1]):
    print("TRIUNGHI")
    print("I = {", points[2].roll, points[3].roll, points[0].roll, "}")
    print("J = {", points[1].roll, "}")

elif inauntru(points[3], points[0], points[1], points[2]):
    print("TRIUNGHI")
    print("I = {", points[3].roll, points[0].roll, points[1].roll, "}")
    print("J = {", points[2].roll, "}")

else:
    a, b, c = lineFromPoints(points[0], points[1])
    k = points[2].x * a + points[2].y * b + c
    q = points[3].x * a + points[3].y * b + c
    if k < 0 and q < 0:
        print("PATRULATER")
        print("I = {", points[0].roll, points[2].roll, "}")
        print("J = {", points[1].roll, points[3].roll, "}")
    else:
        print("PATRULATER")
        print("I = {", points[0].roll, points[1].roll, "}")
        print("J = {", points[2].roll, points[3].roll, "}")
