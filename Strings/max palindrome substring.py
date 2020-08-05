new = []
def subString(string, n):
    for i in range(n):
        for len in range(i+1, n+1):
            print(string[i: len])

string = "aba"
#subString(string, len(string))
new.append(subString(string, len(string)))
print(new)
for i in range(len(new)):
    if new[i] == new[::-1]:
        print(new[i])
