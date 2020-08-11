def lcs(x,y,m,n):
    if m == 0 or n == 0:
        return 0
    elif x[m-1] == y[n-1]:
        return 1 + lcs(x,y, m-1, n-1)
    else:
        return max(lcs(x,y,m-1,n), (lcs(x,y,m,n-1)))

x = input()
y = input()
m = len(x)
n = len(y)
print(lcs(x,y,m,n))