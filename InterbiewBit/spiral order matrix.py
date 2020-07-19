def spiralIndex(arr, m, n):
    k =0
    l = 0

    # k = starting row index
    #l = starting coloumn index
    # m = ending row index
    #n = ending coloumn index

    while (k<m and l<n):
        for i in range(l, n):
            print(arr[k][i], end = " ")
        k += 1

        for i in range(k, m):
            print(arr[i][n-1], end = " ")

        n -= 1

        if (k < m):
            for i in range(n-1, (l-1), -1):
                print(arr[m-1][i], end = " ")
            
            m -= 1

        if (l < n):
            for i in range(m-1, (k-1), -1):
                print(arr[i][l], end = " ")
            
            l += 1

arr = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18] ] 

r = 3
c = 6

print(spiralIndex(arr, r, c))


