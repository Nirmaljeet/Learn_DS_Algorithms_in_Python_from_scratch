from array import *
arr = array('i', [])

n = int(input())
t = int(input())
for i in range(n):
    x = int(input())
    arr.append(x)
    if arr[i] == t:
        print("True")
    else:
        print("False")



print(arr)

