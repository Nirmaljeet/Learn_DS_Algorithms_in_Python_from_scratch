def TwoStrings(str1, str2):
    c = (str1 & str2)
    if len(c) != 0:
        return("YES")
    else:
        return("NO")
n = int(input())
for i in range(n):
    str1 = set(input())
    str2 = set(input())
    result = TwoStrings(str1, str2)
    print(result)