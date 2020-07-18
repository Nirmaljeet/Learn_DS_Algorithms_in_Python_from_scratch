n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)


numbers.sort()
print(*numbers, sep = "\n")
