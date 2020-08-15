def leftRotationbyOne(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def leftRotate(arr,n,d):
    for i in range(d):
        leftRotationbyOne(arr,n)

def printArray(arr,n):
    for i in range(n):
        print(arr[i],end = " ")


nd = input().split()
n = int(nd[0])
d = int(nd[1])
arr = list(map(int, input().rstrip().split()))

leftRotate(arr,n,d)
printArray(arr,n)