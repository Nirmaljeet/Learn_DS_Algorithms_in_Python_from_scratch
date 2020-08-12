def sorting(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr.index(target)
arr = []
n = int(input())

arr = list(map(int, input().split(' ')))
target = int(input())
print(sorting(arr, target))