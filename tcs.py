def findMin(num):
    min=9
    while(num!=0):
        r = num%10
        min = r if r<min else min
        num = num //10
    return min
list =[23,46,745,342]
print (sum(findMin(i) for i in list))
