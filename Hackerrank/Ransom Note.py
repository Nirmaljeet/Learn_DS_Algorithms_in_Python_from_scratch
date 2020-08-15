def stringCheck(string, substring):
    if (string.find(substring)==-1):
        return("No")
    else:
        return("Yes")

mn = input().split()
m = int(mn[0])
n = int(mn[1])
string = input()
substring = input()

print(stringCheck(string, substring))