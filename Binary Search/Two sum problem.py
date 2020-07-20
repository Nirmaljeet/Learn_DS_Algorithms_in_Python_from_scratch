n = int(input())
arr = []
for i in range(0, n):
    t = int(input())
    arr.append(t)

def sum(arr, target):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

target = int(input())
print(sum(arr, target)) 