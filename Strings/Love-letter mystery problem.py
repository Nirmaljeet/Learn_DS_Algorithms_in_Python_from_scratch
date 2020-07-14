
t = int(input())
for i in range(t):
    string = input()
    reverse = string[::-1]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    n = len(string)
    a = list(string)
    b = list(reverse)
    c = list(alphabet)
    e = []
    for i in range(0, n):
        d = abs(alphabet.index(string[i]) - alphabet.index(reverse[i]))
        e.append(d)
    count = 0
    for i in range(0, len(e)):
        count = e[i] + count
    print(int(count/2))
    