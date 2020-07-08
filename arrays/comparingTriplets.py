from array import *

arr1 = array('i', [])
arr2 = array('i', [])

n = int(input("Enter the value for array : "))
for i in range(n):
    x = int(input("Enter the value: "))
    arr1.append(x)
print("Enter the values for array 2 : ")

for i in range(n):
    x = int(input("Enter the value: "))
    arr2.append(x)

a = 0
b = 0
for i in range(n):
    if arr1[i] > arr2[i]:
        a += 1
    if arr1[i] == arr2[i]:
        a += 0
    else:
        b += 1
print(a, b)

        
