a = [[1,2,3],
    [3,4,5],
    [6,7,8]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = " ")
    print()

s1 = a[0][0] + a[1][1] + a[2][2]
s2 = a[2][0] + a[1][1] + a[0][2]
s3 = s2 - s1
print(s3)