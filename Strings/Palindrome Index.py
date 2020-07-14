n = int(input())
for i in range(n):
    string = input()
    reverse = string[::-1]
    a = list(string)
    b = list(reverse)
    
    if string[i] != reverse[i]:
        print(a.index(reverse[i]))
    else:
        print(-1)
    
    if string[i+1] == string[i+2]:
        print(a.index(string[i]))