def binarySearch (arr, l, r): 

	if r >= l: 

		mid = l + (r - l)//2
  
		if arr[mid] == mid: 
			return mid 
		elif arr[mid] > mid: 
			return binarySearch(arr, l, mid-1) 
		else: 
			return binarySearch(arr, mid + 1, r) 
            
	else: 
		return -1

arr = [ -7, -1, 0, 2, 4, 6, 7 ]

result = binarySearch(arr, 0, len(arr)-1) 

if result != -1: 
	print ("Element is present at index", result)
else: 
	print ("Element is not present in array")
