string = input()
stack = []

for i in range(0, len(string)):
    if string[i] == ['h', 'a', 'c', 'k', 'e', 'r', 'n']:
        stack.append(string[i])
        print(stack)