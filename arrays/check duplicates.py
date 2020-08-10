def duplicate(arr, n):
    for i in range(n-1):
        for j in range(i+1, n):
            
            
            if arr[i] == arr[j]:
                #return (arr[i], arr[j])
                return True
arr = [1,2,2,3,4]
n = len(arr)
print(duplicate(arr, n))