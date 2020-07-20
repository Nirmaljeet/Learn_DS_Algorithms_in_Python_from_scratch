def binarySearch(arr, x, n):
    for i in range(0, n):
        if arr[i] == x:
            return arr.index(arr[i])

        if arr[i] > x:
            return arr.index(arr[i])

        if arr[i] < x:
            return len(arr) 
x = int(input())
n = int(input())
arr = []
for i in range(0, n):
    t= int(input())
    arr.append(t)
result = binarySearch(arr, x, n)
print(result)