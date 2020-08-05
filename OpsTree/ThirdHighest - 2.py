n = int(input("Enter the number: "))
arr = []
for i in range(0, n):
    x = int(input("Enter the values: "))
    arr.append(x)

print(arr)
new = []
def ThirdHighest(arr, n):
    for i in range(0, n-1):
        if arr[i+1] > arr[i]:
            new.append(arr[i+1])
    print(new)
    if len(new) < 3:
        print("Invalid")

    else:
        print(new[0])

print(ThirdHighest(arr, n))