def sum(arr,target):
    	for i in range(0, len(arr)-3):
		for j in range(i+1, len(arr)-2):
			for k in range(j+1, len(arr)-1):
				for l in range(k+1, len(arr)):
					if arr[i]+arr[j]+arr[k]+arr[l] == target:
						print(arr[i], arr[j], arr[k], arr[l])
					
arr = [1, 0, -1, 0, -2, 2]
target = 0
print(sum(arr, target))