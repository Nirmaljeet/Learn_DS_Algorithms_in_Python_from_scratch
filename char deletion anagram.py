chars = 26

def anagrams(str1, str2):
    count1 = [0]*chars
    count2 = [0]*chars

    i = 0
    for i in range(len(str1)):
        count1[ord(str1[i])-ord('a')] += 1
        i+=1

    i = 0
    for i in range(len(str2)):
        count2[ord(str2[i])-ord('a')] += 1
        i+=1
    res = 0
    for i in range(26):
        res += abs(count1[i]-count2[i])
    return count1
    return count2
str1 = "bcadeh"
str2 = 'hea'
print(anagrams(str1, str2))