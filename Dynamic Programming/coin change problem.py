def count(S, m, n):
    table = [0 for k in range(n+1)]
    table[0] = 1
    for i in range(m):
        for j in range(S[i], n+1):
            table[j] += table[j-S[i]]

    return table[n]

S = [1,2,3]
n = 4
m = len(S)

print(count(S, m, n))