from array import *
integers = array('i', [])
n, s = map(int, input("Enter the number of integers and sum: ").split())
for i in range (0, n):
    x = int(input('Enter the integers: '))
    integers.append(x)


count = 0
for i in range(0, n):
    for j in range(i+1, n):
        if((integers[i]+integers[j])%s==0):
            count +=1
print(count)
