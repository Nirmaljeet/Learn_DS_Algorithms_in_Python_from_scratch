def commonchild(str1, str2):
    a = list(str1)
    b = list(str2)
    count = 1
    for i in range(0, len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c = str1.index(a[i])
                d = str2.index(b[j])
                for r in range(c, len(a)):
                    for s in range(d, len(b)):
                        if a[r] == b[s]:
                            count += 1
            
    return count

str1 = "abcdef"
str2 = "fbdamn"
print(commonchild(str1, str2))