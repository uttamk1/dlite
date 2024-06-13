x=int(input("Enter marks "))
y=int(input("Enter marks "))

list = []
for i in range(x,y):
    sum=0
    n=len(str(i))
    for count in range(0,n):
        sum += pow(int(str(i)[count]),n)
    if sum == i:
        list.append(i)
        print(f"{i} appended")
print(list)