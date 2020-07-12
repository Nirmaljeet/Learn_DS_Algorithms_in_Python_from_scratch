n = int(input("Enter the number: "))
string = input("Enter the string: ")
rotate = int(input("Enter the times string is rotated: "))

Lfirst = string[0: rotate]
Lsecond = string[rotate: ]
newString = Lsecond + Lfirst
print(newString)

for i in range(0, n):
    #print(string[i])
    #print(newString[i])
    string[i] == newString[i]
    print(string)
    print(newString)