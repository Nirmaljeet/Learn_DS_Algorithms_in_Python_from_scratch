stack = []
n = int(input("Enter the number of elements you want to enter in the stack"))

for i in range(0,n) :
    ele = int(input("Enter the elements"))
    stack.append(ele)
    print("This is the initial slack : ", stack)
    continue
print("Now we are deleting the elements :")
print(stack.pop())
print(stack.pop())
print("The current stack is as follows : ")
print(stack)