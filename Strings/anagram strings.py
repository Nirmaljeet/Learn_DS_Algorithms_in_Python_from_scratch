str1 = "bca"
str2 = "acb"

str1 = sorted(str1)
str2 = sorted(str2)

n1 = len(str1)
n2 = len(str2)

count = 0
for i in range(n1):
    for j in range(n2):
        if list(str1[i]) == list(str2[j]):
            print(abs(len(str1)-len(str2)))