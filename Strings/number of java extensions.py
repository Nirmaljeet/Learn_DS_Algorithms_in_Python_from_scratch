def javafind(str1, str2):
    count = 0
    res = str1.split('.')
    if res[-1] == 'java':
        count += 1
    res1 = str2.split('.')
    if res1[-1] == 'java':
        count += 1
    return count
str1 = "nirmaljeet.java"
str2 = "abc"
print(javafind(str1,str2))