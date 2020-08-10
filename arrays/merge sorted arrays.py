arr = [1,2,3]
arr2 = [2,5,6]
new = []
for i in range(len(arr)):
    new.append(arr[i])
    

for i in range(len(arr2)):
    new.append(arr2[i])
new.sort()
print(new)
