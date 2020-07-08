from array import *

arr = array('i', [])
n = int(input("Enter the number of students: "))
for i in range(n):
    x = int(input("Enter the marks: "))
    arr.append(x)

for i in range(n):
    if arr[i] < 38:
        print(arr[i])
        

    elif arr[i] % 5 == 0:
        print(arr[i])
        

    elif ((arr[i] + 2) % 5 == 0):
        print(arr[i] + 2)

    elif ((arr[i] + 1) % 5 == 0):
        print(arr[i] + 1)
        

    elif ((arr[i] + 2) % 5 != 0):
        print(arr[i])
        
    