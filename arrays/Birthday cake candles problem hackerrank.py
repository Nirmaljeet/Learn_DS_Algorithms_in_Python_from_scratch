from array import *
arr = array('i', [])

n = int(input("Enter the candles/age : "))
for i in range(n):
    x = int(input("Enter the values: "))
    arr.append(x)

for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

count = 0
for i in range(n):
    if arr[i] == arr[n-1]:
        count += 1
        
print(count)
