import re
n = int(input())
string1 = input()
number = 0
lower = 0
upper = 0
charachter = 0


    
for a in string1:
    if (a.isupper()) == True:
        upper = 1

    if (a.islower()) == True:
        lower = 1

    if (a.isnumeric()) == True:
        number = 1

   
    



regex = re.compile('["!@#$%^&*()-+"]')

if(regex.search(string1) == None): 
        charachter = 0
else:
    charachter = 1
          



total = number + charachter + lower + upper
need = 4-total



abc = max(need, 6-n)
print(abc)
    

