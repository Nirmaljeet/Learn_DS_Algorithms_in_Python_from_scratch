from array import *

size = array('i', [])

n = int(input("Enter the number of chocolate blocks: "))
for i in range(0, n):
    x = int(input("Enter the integers: "))
    size.append(x)

d = int(input("Enter the day: "))
m = int(input("Enter the month: "))

count = 0

for i in range(0, n):
    
    if(size[i] + size[m-1] == d):
        count = count + 1

print(count)