from array import *

arr = array('i', [ ])
n = int(input("Enter the number: "))



for i in range(0, n-1):
   
    x = int(input("Enter the length: "))
    arr.append(x)
    
for i in range(0, n-2):
    if (arr[i] + 1 != arr[i+1]):
        print(arr[i]+1)