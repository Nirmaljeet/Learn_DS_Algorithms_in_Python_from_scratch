def zigzagconversion(string, n):
    if n == 1:
        print(string)
        return

    l = len(string)

    arr = ["" for x in range(l)]
    row = 0
    for i in range(l):
        arr[row] += string[i]
        if row == n-1:
            down = False

        elif row == 0:
            down = True

        if down:
            row += 1
        else:
            row -= 1

    for i in range(n):
        print(arr[i], end = "")

string = "GEEKSFORGEEKS"
n = 3
print(zigzagconversion(string, n))