charachters = 256
def longestSubsequence(string):
    i = 0
    lastIndex = [-1]*charachters
    res = 0
    for j in range(len(string)):
        i = max(i, lastIndex[ord(string[j])] + 1)
        res = max(res, j-i+1)
        lastIndex[ord(string[j])] = j
    return res

string = input()
print(longestSubsequence(string))