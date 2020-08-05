n = int(input("Number of values: "))
arr = []
for i in range(0, n):
    x = int(input("Enter the values: "))
    arr.append(x)

print("initial array is: ", arr)

arr.sort()
print("Sorted array is:", arr)

sum = 0
for i in range(0, n-1):
    sum = sum + arr[i]
print(sum)

for i in range(0, n-1):
    temp = arr[n-1]
print(temp)

if temp == sum:
    print("True")
else:
    print("False")