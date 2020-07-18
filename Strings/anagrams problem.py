n = int(input())
for i in range(n):
    string = input()
    a = list(string)
    s1 = len(string)//2
    s2 = (len(string)+1)//2 
    print(s1, s2)

    for char in string:
        print(char)