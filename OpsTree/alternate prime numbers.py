def primeNumber(num):
    a = 0
    for i in range(2, num //2 + 1):
        if num %i == 0:
            a = 1
            break

    if a == 0:
        return 1
    else:
        return 0

def PrintNum(n):
    count = 0

    for num in range(2, n):
        if primeNumber(num) == 1:
            if count %2 == 0:
                print(num, end = " ")
            count += 1

if __name__ == "__main__":
    n = 17

    print("Numbers: ")
    PrintNum(n)