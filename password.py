pswd = input("Enter password: ")
l = 0
u = 0
sp1 = 0
s = 0
d = 0

if len(pswd) > 7:
    for i in pswd:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i.isdigit():
            d += 1
        elif i.isspace():
            s += 1
        else:
            sp1 += 1

    if l > 0 and u > 0 and sp1 > 0 and d > 0 and s == 0:
        print('Valid Password')
    else:
        print('Invalid Password')
else:
    print('Password length should be at least 8 characters.')
