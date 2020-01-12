def largestKSubmatrix(a):

    Row = len(a)
    Col = len(a[0])
    
    dp = [[0 for x in range(Col)] for y in range(Row)] 
  
    result = 0
    I = -1
    J = -1
    for i in range(Row): 
        for j in range(Col): 
              
            if (i == 0 or j == 0): 
                dp[i][j] = 1
  
            else: 
                  
                if (a[i][j] == 0 and
                    a[i][j] == a[i - 1][j] and
                    a[i][j] == a[i][j - 1] and
                    a[i][j] == a[i - 1][j - 1]): 
                      
                    dp[i][j] = min(min(dp[i - 1][j],  
                                       dp[i][j - 1]), 
                                       dp[i - 1][j - 1] ) + 1
                else: 
                    dp[i][j] = 1

            if result < dp[i][j]:
                I = i
                J = j

            result = max(result, dp[i][j])

    v = [0 for i in range(result + 1)]

    for i in range(Row):
        for j in range(Col):
            if dp[i][j] != 1:
                for k in range(2, dp[i][j] + 1):
                    v[k] += 1
    
    for i in range(Row):
        print(dp[i])

    return result, I - result + 1, J - result + 1, v

a = [[ 0, 0, 1, 1, 0, 1 ], 
     [ 0, 0, 0, 0, 0, 1 ], 
     [ 0, 1, 0, 0, 0, 1 ], 
     [ 0, 1, 0, 0, 0, 1 ]]
  
print(largestKSubmatrix(a)) 


  