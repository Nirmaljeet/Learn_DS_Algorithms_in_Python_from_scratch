from array import *
arr = array('i', [])

n = int(input("Enter the length of array: "))
for i in range(n):
    x = int(input("Enter the values: "))
    arr.append(x)

for i in range(n):
    for j in range(i+1, n):
        if(arr[i] > arr[j]):
            temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
max = 0
for i in range(1, n):
    max = max + arr[i]

min = 0
for i in range(0, n-1):
    min = min + arr[i]

print(max, min)

