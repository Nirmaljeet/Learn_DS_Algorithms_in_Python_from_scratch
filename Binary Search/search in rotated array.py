def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def leftRotate(arr, n, d):
    for i in range(d):
        leftRotatebyOne(arr, n)

def printArray(arr, size):
    for i in range(size):
        print("%d"% arr[i], end = " ")

def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = []
n = int(input())
d = int(input())
for i in range(n):
    x = int(input())
    arr.append(x)

target = int(input())

leftRotate(arr, n, d)
print(printArray(arr, len(arr)))
print(search(arr, target))