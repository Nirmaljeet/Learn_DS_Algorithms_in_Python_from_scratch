def stringConstruction(str1):
    a = list(str1)
    b = []
    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])
        
    return len(b)

n = int(input())
for i in range(n):
    str1 = input()
    result = stringConstruction(str1)
    print(result)