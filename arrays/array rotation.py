import array
arr = array.array('i', [1,2,3,4,5,6,7])
for i in range(0, 7):
    print(arr[i])

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
        print(arr[i])
print('Array after rotation is: ')
leftRotate(arr, 2, 7)
printArray(arr, 7)