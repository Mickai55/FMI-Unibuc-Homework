def isPrime(n) : 
  
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True
    if (n % 2 == 0 or n % 3 == 0): 
        return False
    i = 5
    while(i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6
    return True

def findCombinationsUtil(arr, index, num, reducedNum): 
  
    if (reducedNum < 0): 
        return; 
  
    if (reducedNum == 0): 
  
        for i in range(index): 
            print(arr[i], end = " ")
        print("")
        return

    prev = 1 if(index == 0) else arr[index - 1]
  
    for k in range(prev, num + 1): 
        if isPrime(k):
            arr[index] = k
            findCombinationsUtil(arr, index + 1, num, reducedNum - k)
  
 
def findCombinations(n): 
      
    arr = [0] * n; 
    findCombinationsUtil(arr, 0, n, n); 
  
n = 17
findCombinations(n)

# prm = []

# for i in range(n):
#     if isPrime(i):
#         prm.append(i)
