def maxSum(arr, n):
    max_till_here = 0
    max_ending_here = 0
    for i in range(0, n):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif(max_till_here < max_ending_here):
            max_till_here = max_ending_here
    return max_till_here

arr = [1,2,3,4,-5]
n = len(arr)
print(maxSum(arr, n))