import math
import matplotlib.pyplot as plt
import numpy as np

def define_circle(p1, p2, p3):
    """
    Returns the center and radius of the circle passing the given 3 points.
    In case the 3 points form a line, returns (None, infinity).
    """
    temp = p2.x * p2.x + p2.y * p2.y
    bc = (p1.x * p1.x + p1.y * p1.y - temp) / 2
    cd = (temp - p3.x * p3.x - p3.y * p3.y) / 2
    det = (p1.x - p2.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p2.y)

    if abs(det) < 1.0e-6:
        return (None, np.inf)

    # Center of circle
    cx = (bc*(p2.y - p3.y) - cd*(p1.y - p2.y)) / det
    cy = ((p1.x - p2.x) * cd - (p2.x - p3.x) * bc) / det

    radius = np.sqrt((cx - p1.x)**2 + (cy - p1.y)**2)
    return (cx, cy, radius)

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

A.append(Point(0, 0))
A.append(Point(0, 4))
A.append(Point(4, 0))
A.append(Point(4, 88))

a1, b1, c1 = lineFromPoints(A[0], A[2])
a2, b2, c2 = lineFromPoints(A[1], A[3])

delta = a1 * b2 - b1 * a2

convex = 0

if delta:
    x = ((-c1 * b2) - (b1 * -c2)) / delta
    y = ((a1 * -c2) - (-c1 * a2)) / delta
    
    #print(x, y)

    if x < max(A[0].x, A[2].x) and x > min(A[0].x, A[2].x) and y < max(A[0].y, A[2].y) and y > min(A[0].y, A[2].y) and x < max(A[1].x, A[3].x) and x > min(A[1].x, A[3].x) and y < max(A[1].y, A[3].y) and y > min(A[1].y, A[3].y):
        convex = 1
        print("Convex.")
    else:
        convex = 0
        print("Nu e convex.")
else:
    print("Nu e convex.")


if convex == 1:
    P01 = distance(A[0], A[1])
    P02 = distance(A[0], A[2])
    P12 = distance(A[1], A[2])
    angle1 = math.acos((pow(P01, 2) + pow(P12, 2) - pow(P02, 2)) / (2 * P01 * P12))

    P03 = distance(A[3], A[0])
    P32 = distance(A[3], A[2])
    P02 = distance(A[0], A[2])
    angle2 = math.acos((pow(P03, 2) + pow(P32, 2) - pow(P02, 2)) / (2 * P03 * P32))

    #print(angle1, angle2, math.pi)

    if angle1 + angle2 == math.pi:
        print("A4 e pe cerc.")
    elif angle1 + angle2 > math.pi:
        print("A4 e in interiorul cercului.")
    else:
        print("A4 e in exteriorul cercului.")

# plt.figure()
# # plt.axis([-5, 5, -5, 5])
# x = np.linspace(-5, 5, 1000)
# plt.scatter(0, 0, color="red")
# plt.plot(x, np.sqrt(25 - x**2), color="blue")
# plt.plot(-x, -np.sqrt(25 - x**2), color="blue")
# ####################################cerc cu centrul in 0, 0
# plt.show()

x, y, r = define_circle(A[0], A[1], A[2])

circle = plt.Circle((x, y), r, color='blue', fill = 0)

fig, ax = plt.subplots()
ax.set_xlim((-1, 5))
ax.set_ylim((-1, 5))

ax.add_artist(circle)
# ax.plot([A[0].x, A[1].x], [A[0].y, A[1].y], color = "blue")
# ax.scatter(x, y, color="blue")
ax.scatter(A[0].x, A[0].y, color="red")
ax.scatter(A[1].x, A[1].y, color="red")
ax.scatter(A[2].x, A[2].y, color="red")
ax.scatter(A[3].x, A[3].y, color="red")

plt.show()