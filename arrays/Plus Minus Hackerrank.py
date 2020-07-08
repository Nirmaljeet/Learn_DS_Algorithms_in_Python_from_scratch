from array import *
arr = array('i', [ ])

n = int(input("Enter the length of array: "))

for i in range(n):
    x = int(input("Enter the value: "))
    arr.append(x)

positive = 0
negative = 0
zeros = 0

for i in range(n):
    if arr[i] > 0:
        positive += 1
    if arr[i] == 0:
        zeros += 1
    if arr[i] < 0:
        negative += 1

positiveRatio = positive/n
negativeRatio = negative/n
zeroRatio = zeros/n

print(positiveRatio, negativeRatio, zeroRatio)
