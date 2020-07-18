def leftRotate(arr, d ,n):
    for i in range(d):
        leftRotatebyOne(arr, n)

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printArray(arr, size):
    for i in range(size):
        print(arr[i], end = " ")

n = int(input())
d = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

leftRotate(arr, 2, len(arr))
printArray(arr, len(arr))