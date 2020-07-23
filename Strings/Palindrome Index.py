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
    
    
    