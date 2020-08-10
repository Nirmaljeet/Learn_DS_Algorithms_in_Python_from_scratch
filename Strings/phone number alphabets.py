from itertools import combinations
num_2 = 'abc'
num_3 = 'def'
num_4 = 'ghi'
num_5 = 'jkl'
num_6 = 'mno'
num_7 = 'pqrs'
num_8 = 'tuv'
num_9 = 'wxyz'


target = num_2+num_3
print(target)

comb = combinations(list(target),2)
for i in list(comb):
    print(i)