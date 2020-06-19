s = " xyzzzzxy"
dict = set({"xyz", "zzz", "zzzz","x" , "y", "xy"})
prev, L = [],[]
def spaces(s, dict):
    n = len(s)
    global prev, L
    L = [-1] * (n)
    prev = [-1] * (n)
    L[0] = 0
    for i in range(1,n):
         for j in range(i, 0, -1):
            if s[j:i+1] in dict: #dict.__contains__( s[j:i+1])
                if((L[j-1]+1 < L[i] or L[i]==-1) and L[j-1]!=-1):
                    L[i] = L[j - 1] + 1
                    prev[i] = j - 1
    return L[n - 1]
def print_substr(i):
    if prev[i] > 0:
        print_substr(prev[i])
    print( s[prev[i] + 1 : i + 1] )
print(spaces(s, dict))
print_substr(len(s) - 1)