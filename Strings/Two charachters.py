from itertools import combinations



n = int(input("Enter the length: "))

string = input("Enter the string: ")

comb = combinations([len(string)], 2)
for i in list(comb):
    print(i)


stack = []
stack.append(string)

print(stack)
