pswd = input("Enter username: ")
l = 0
u = 0
sp1 = 0
s = 0
d = 0
sp=0
if pswd[0].isalpha():
    if len(pswd) > 4:
        for i in pswd:
            if i.islower():
                l += 1
            elif i.isupper():
                u += 1
            elif i.isdigit():
                d += 1
            elif i.isspace():
                s += 1
            elif i =='.' or i == '_':
                sp += 1
            else:
                sp1 += 1

        if l > 0 and u == 0 and sp1 == 0 and d >= 0 and s == 0:
            print('Valid username')
        else:
            print('Invalid username')
    else:
        print('username length should be at least 8 characters.')
else:
    print('Invalid username. starts with number')
