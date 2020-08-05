n = int(input("Enter the length: "))
arr = []
for i in range(0, n):
    x = int(input("Enter the values: "))
    arr.append(x)

print(arr)

arr.sort()

if len(arr) > 3:
    for i in range(0, n):
        highest = arr[n-3]
    print("Third Highest number is: ", highest)

else:
    print("Array length is not sufficient")