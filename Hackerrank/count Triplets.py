def countTriplets(arr):
    new = []
    count = 0
    for i in range(0, len(arr)-2):
        for j in range(1, len(arr)-1):
            for k in range(2,len(arr)):
                new.append(arr[i])
                new.append(arr[j])
                new.append(arr[k])
    for i in range(len(new)-2):
        if new[i+1] == new[i]*r and new[i+2] == new[i]*r*r:
            count += 1
    return count

mr = input().split()
m = int(mr[0])
r = int(mr[1])

arr = list(map(int, input().rstrip().split()))

print(countTriplets(arr))