arr = [5,5,25,25,125]
count = 0
new = []
for i in range(0, len(arr)-2):
    for j in range(1, len(arr)-1):
        for k in range(2,len(arr)):
            new.append(arr[i])
            new.append(arr[j])
            new.append(arr[k])
for i in range(len(new)-2):
    if new[i+1] == new[i]*5 and new[i+2] == new[i]*5*5:
        count += 1
print(count)