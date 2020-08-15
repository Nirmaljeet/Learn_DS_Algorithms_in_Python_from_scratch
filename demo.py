def arrayRotate(arr,d):
    return arr[d:] + arr[:d]

nd = input().split()
n = int(nd[0])
d = int(nd[1])

arr = list(map(int, input().rstrip().split()))

result = arrayRotate(arr,d)
print(result)