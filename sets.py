from sets import *
def Subsequence(arr, n):

    s = set()
    count = 0

    for element in arr:
        s.add(element)

    for i in range(n):
        if (arr[i] - 1) not in s:
            j = arr[i]
            while(j in s):
                j += 1

            count = max(count, j-arr[i])
    return count

if __name__ == "__main__":
    n = 7
    arr = [49,1,3,200,2,4,70,5]

    print("The length is: ")
    print(Subsequence(arr, n))