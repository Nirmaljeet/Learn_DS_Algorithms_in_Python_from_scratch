from itertools import permutations

def allpermutations(arr):
    permList = permutations(arr)
    for perm in list(permList):
        print(perm)
arr = [1,2,3]
print(allpermutations(arr))