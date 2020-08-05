
def nextNum(value, n):
    for i in range(n-1, 0, -1):
        if value[i] > value[i-1]:
            break

    if i == 1 and value[i] <= value[i-1]:
        print("Error -> value not possible: ")
        return
    print(value[i])
    x = value[i-1]
    less = i

    for j in range(i+1, n):
        if value[j] > x and value[j] < value[less]:
            less = j


    value[less], value[i-1] = value[i-1], value[less]

    x = 0

    for j in range(i):
        x = x*10 + value[j]


    value = sorted(value[i:])

    for j in range(n-i):
        x = x*10 + value[j]

    print("New Number is as follows: ", x)
    
numbers = '239872'
value = list(map(int, numbers))
nextNum(value, len(numbers))