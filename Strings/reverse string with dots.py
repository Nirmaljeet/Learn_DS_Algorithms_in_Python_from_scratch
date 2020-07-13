value = int(input())
for i in range(0, value):
    string = input().split('.')
    new_string = []
    for s in range(len(string)-1, -1, -1):
        new_string.append(string[s])
    print('.'.join(new_string))
        
    