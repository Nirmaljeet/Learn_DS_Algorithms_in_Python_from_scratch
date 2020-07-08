import math

x1 = int(input("Starting point of kangaroo 1: "))
v1 = int(input("Jump of kangaroo 1: "))
x2 = int(input("Starting point of kangaroo 2: "))
v2 = int(input("Jump of kangaroo 2: "))

sum1 = 0
sum2 = 0
c = 1000
for i in range (c):
    sum1 =  x1 + v1*i
    sum2 =  x2 + v2*i
if sum1 == sum2:
    print('YES')
else:
    print('NO')
print(sum1)
print(sum2)