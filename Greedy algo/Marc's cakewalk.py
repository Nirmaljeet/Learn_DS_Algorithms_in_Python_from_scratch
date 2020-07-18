from itertools import *
arr = []
new = []
n = int(input())
for i in range(n):
    x = int(input())
    arr.append(x)

perm = permutations(arr, len(arr))

for i in list(perm):
    
    new.append(i)
print(new)

print(2*new[1].map(2))