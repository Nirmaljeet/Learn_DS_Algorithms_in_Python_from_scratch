arr = [2,1,3,1,2]
count = 0
for j in range(len(arr)):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count += 1
            print(arr)
print(count)