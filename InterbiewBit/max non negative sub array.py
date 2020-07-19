n = int(input())

arr = []
for i in range(0, n):
    x = int(input())
    arr.append(x)
print(arr)

sum = 0
new_sum = 0
for i in range(0, len(arr)):
    if arr[i] > 0:

        sum = sum + arr[i]


    if arr[i] < 0:

        for i in range(arr[i], len(arr)):


        
            if arr[i+1] > 0:
                new_sum = new_sum + arr[i+1]

            if arr[i+1] > len(arr) - 1:
                break
        print(new_sum)
    if new_sum > sum:
        print(new_sum)
    if sum > new_sum:
        print(sum)
