# a super market maintains a price format  for all its products. a value n
n = 5244
sum = 1
while n>0:
    sum+= n%10
    n//=10
print(sum)