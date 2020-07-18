from itertools import combinations

n = int(input())
arr = []
new = []
for i in range(0, n):
    x = int(input())
    arr.append(x)



comb = combinations(arr, 2)
for i in list(comb):
    
    new.append(abs(i[1] - i[0]))
print(min(new))