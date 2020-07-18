n = int(input())
t = int(input())

def lex(string):
     if list(string) == sorted(string):
            print('YES')
     else:
            print('NO')
if __name__ == '__main__':
    new = []
    for i in range(t):
        string = input()
        new.append(string)
    
    print(lex(string))