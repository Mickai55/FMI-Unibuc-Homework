v = [j for j in range(12345563)]

def minmax(v, i, j):
    if j - i <= 1:
        return (min(v[i], v[j]), max(v[i], v[j]))
        
    else:
        min_st, max_st = minmax(v, i, (i + j) // 2)
        min_dr, max_dr = minmax(v, (i + j) // 2 + 1, j)
        
        return min(min_st, min_dr), max(max_st, max_dr)

print(minmax(v, 0, len(v) - 1))
