def search(num, n):
    for i in range(n-1, 0, -1):
        if num[i] > num[i-1]:
            break

    if i == 1 and num[i] <= num[i-1]:
        print("Not Possible")
        return
        

    a = num[i-1]
    small = i

    for j in range(i+1, n):
        if num[j] > a and num[j] < num[small]:
            small = j

            
    num[small], num[i-1] = num[i-1], num[small]

    a = 0

    for j in range(i):
        a = a*10 + num[j]

    num = sorted(num[i:])

    for j in range(n-i):

        a = a*10 + num[j]

    print("New number is: ", a)

ans = "1234567"
num = list(map(int, ans))

print(search(num, len(ans)))