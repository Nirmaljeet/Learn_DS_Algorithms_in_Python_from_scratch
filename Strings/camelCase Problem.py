string1 = input("Enter the string: ")
count = 0
for a in string1:
    if (a.isupper()) == True:
        count += 1

print(count + 1)