n = int(input(""))
string = input("")
rotate = int(input(""))

Lfirst = string[0: rotate]
Lsecond = string[rotate: ]
newString = Lsecond + Lfirst
print(newString)

