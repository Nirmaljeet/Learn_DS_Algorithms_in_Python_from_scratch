def sum(arr, n):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == n:
                return arr.index(arr[i]), arr.index(arr[j])

arr = []
n = int(input())
x = int(input())
for i in range(x):
    t = int(input())
    arr.append(t)

print(sum(arr, n))
