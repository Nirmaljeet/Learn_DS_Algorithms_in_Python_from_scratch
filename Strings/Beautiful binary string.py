n = int(input())
arr = list(input())
count = 0
for i in range(0, n-1):
    x = int(input())
    arr.append(x)
for i in range(0, len(arr)-2):
    if (arr[i] == 0 and arr[i+1] == 1 and arr[i+2] == 0):
        count += 1
print(count)

