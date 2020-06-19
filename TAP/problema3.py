def findMedian(a, n, b, m): 
  
    min_index = 0 
    max_index = n  
       
    while min_index <= max_index: 

        i = (min_index + max_index) // 2
        j = (n + m + 1) // 2 - i
       
        if i < n and j > 0 and b[j - 1] > a[i]: 
            min_index = i + 1
        elif i > 0 and j < m and b[j] < a[i - 1]: 
            max_index = i - 1
        else : 
            if i == 0: 
                median = b[j - 1] 
            elif j == 0: 
                median = a[i - 1]          
            else : 
                median = max(a[i - 1], b[j - 1])  
            break
          
    if (n + m) % 2 == 1: 
        return median 

    if i == n: 
        return (median + b[j]) / 2.0

    if j == m: 
        return (median + a[i]) / 2.0
       
    return (median + min(a[i], b[j])) / 2.0
  

a = [2, 3, 5, 8, 9] 
b = [10, 11, 12, 14, 16, 18, 20] 

# a = [-5, 3, 6, 12, 15, 100] 
# b = [-12, -10, -6, -3, 4, 10] 

n = len(a) 
m = len(b) 

if (n < m) : 
    print ("The median is :", findMedian(a, n, b, m))
else : 
    print ("The median is :", findMedian(b, m, a, n)) 