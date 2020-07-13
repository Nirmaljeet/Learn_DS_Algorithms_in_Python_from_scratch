def isPangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
        else:
            return True

    string = input()
    if(isPangram(string) == True):
        print('pangram')
    else:
        print('not pangram')

    