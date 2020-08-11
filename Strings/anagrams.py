def anagrams(str):
    n = len(str)//2
    if len(str)%2 != 0:
        return -1
    else:
        str1 = str[0:n]
        str2 = str[n:]
    count = 0
    sorted(str1)
    sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

t = int(input())
for i in range(t):
    str = input()
    result = anagrams(str)
    print(result)