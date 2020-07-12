string = input()

n = int(len(string)/3)


k = 'SOS'*n

count = 0
for i in range(0, len(string)):
    if string[i] != k[i]:
        count += 1
print(count)