l1 = [25,8,'abc',31,48,39,'xyz',37]
l2 = [48,19,'apple',23,'egg',31]
l3 = [29,58,2,'xyz',3,8,7,9,11,5,40,45]

def isprime(a):
    return not any(a % i == 0 for i in range(2, int(a ** 0.5) + 1))
l2p = []
for i in l1:
    if type(i)==int:
        if isprime(i):
            l2p.append(i)
n =max(l2p)
a = min(l2p)
print(l2p)
prime_list = []
for i in range(a, n+1):
    if isprime(i):
        prime_list.append(i)

if l2p == prime_list:
    print("yes")
else:
    print("no")