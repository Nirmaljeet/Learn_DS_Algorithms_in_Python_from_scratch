def sortColors(arr, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] >= arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                i += 1
                j += 1
    return arr
arr = [2,0,2,1,1,0]
n = len(arr)
print(sortColors(arr,n)) 
