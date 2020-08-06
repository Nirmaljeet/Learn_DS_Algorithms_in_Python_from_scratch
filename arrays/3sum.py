def threesum(arr, n):
    for i in range(0, len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == n:
                    print("Triplet is: ", arr[i], arr[j], arr[k])
                    return True
    return False

arr = [-1,0,1,2,-1,-4]
n = 0
print(threesum(arr, n))