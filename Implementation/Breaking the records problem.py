from array import *

scores = array('i', [])

n = int(input("Enter the scores: "))
for i in range(0, n):
    x = int(input(" Enter the number: "))
    scores.append(x)

maxi = scores[0]
mini = scores[0]
max = 0
min = 0

for i in range(0, n):
    if(scores[i]>maxi):
        maxi = scores[i]
        max += 1

    if(scores[i]<mini):
        mini = scores[i]
        min += 1

print(maxi, mini)
        