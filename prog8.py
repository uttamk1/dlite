n=int(input("Enter prime: "))
flag=0
for i in range (2,n):
    if n%i==0:
        print("Not prime")
        flag=1
    else:
        continue
if (flag==0):
    print("prime")