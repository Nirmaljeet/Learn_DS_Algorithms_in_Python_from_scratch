alphabets = "abcdefghijklmnopqrstuvwxyz"
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

stack1 = []
stack2 = []
for i in range(0, len(alphabets)):
    stack1.append(alphabets[i])
print(stack1)

for i in range(0, len(alphabets)):
    stack2.append(numbers[i])
print(stack2)

string = input()
n = int(input())

for i in range(0, n):
    n1 = int(input())
