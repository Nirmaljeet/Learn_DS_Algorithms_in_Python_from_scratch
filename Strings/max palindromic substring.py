from itertools import permutations
def allPermutations(str):
    perms = permutations(str)
    new = []
    for perm in list(perms):
        if perm == perm[::-1]:
            new.append(perm)
            return new
print(allPermutations('babad'))


