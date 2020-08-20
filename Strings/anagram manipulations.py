str1 = "ddcf"
str2 = "cedk"

str1 = sorted(str1)
str2 = sorted(str2)

n1 = len(str1)
n2 = len(str2)

print(str1)
print(str2)

for i in str1:
    for j in str2:
        if i == j:
            print(i,j)