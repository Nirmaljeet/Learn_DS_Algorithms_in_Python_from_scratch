from array import *
apples = array('i', [ ])
oranges = array('i', [ ])
s = int(input("Enter the left location of house: "))
t = int(input("Enter the right position of house: "))
a = int(input("Enter the location of apple tree: "))
b = int(input("Enter the location of orange tree: "))
m = int(input("Enter the no. of apples falling: "))
n = int(input("Enter the number of oranges falling: "))
for i in range(m):
    x = int(input("Enter the locations: "))
    apples.append(x)

for i in range(n):
    y = int(input("Enter the location of oranges: "))
    oranges.append(y)



for i in range(m):
    apples[i] = apples[i] + a
print(apples)



applescount = 0

for i in range(m):
    if (apples[i] >= s) and (apples[i] <= t):
        applescount = applescount +1
    

for i in range(n):
    oranges[i] = oranges[i] + b
print(oranges)

orangescount = 0

for i in range(n):
    if (oranges[i] >= s) and (oranges[i] <= t):
        orangescount = orangescount +1

print(applescount)
print(orangescount)