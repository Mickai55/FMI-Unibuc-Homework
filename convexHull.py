class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
def Left_index(points): 
      
    ''' 
    Finding the left most point 
    '''
    minn = 0
    for i in range(1,len(points)): 
        if points[i].x < points[minn].x: 
            minn = i 
        elif points[i].x == points[minn].x: 
            if points[i].y > points[minn].y: 
                minn = i 
    return minn 
  
def orientation(p, q, r): 
    ''' 
    0 --> p, q and r are colinear  
    1 --> Clockwise  
    2 --> Counterclockwise  
    '''
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y) 
  
    if val == 0: 
        return 0
    elif val > 0: 
        return 1
    else: 
        return 2
  
def convexHull(points, n): 
      
    # There must be at least 3 points  
    if n < 3: 
        return
  
    # Find the leftmost point 
    l = 9
  
    hull = [] 

    p = l 
    q = 0
    while(True): 
          
        # Add current point to result  
        hull.append(p) 
  
        q = (p + 1) % n 
  
        for i in range(n): 
              
            # If i is more counterclockwise  
            # than current q, then update q  
            if(orientation(points[p], points[i], points[q]) == 1): 
                q = i 
  
        p = q 
  
        # While we don't come to first point 
        if(p == l): 
            break
  
    # Print Result  
    for each in hull: 
        print(points[each].x, points[each].y) 
  
# Driver Code 
A = [] 
A.append(Point(1, 0))
A.append(Point(0, 1))
A.append(Point(0, 2))
A.append(Point(1, 3))
A.append(Point(3, 4))
A.append(Point(4, 4))
A.append(Point(6, 2))
A.append(Point(6, 0))
A.append(Point(9, 9))
  
convexHull(A, len(A)) 