def binarySearch(arr, l, r, x):

    if r >= 1:
        mid = 1 + (r-1)//2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        return -1

n = int(input())
arr = []
for i in range(0, n):
    t = int(input())
    arr.append(t)

x = int(input())

result = binarySearch(arr, 0, len(arr)-1, x)
print(result)


