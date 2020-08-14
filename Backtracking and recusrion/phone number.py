table = [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
def phone(table):
    n1 = int(input())
    n2 = int(input())
    
    for i in range(len(table[n1])):
        for j in range(len(table[n2])):
            return list(table[n1][i]) + list(table[n2][j])

print(phone(table))