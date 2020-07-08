from array import *
arr = array('i', [])

n = int(input())
for i in range(n):
    x = int(input())
    arr.append(x)

print(arr)

sum = 0
for i in range(n):
    sum = sum + arr[i]

print(sum)