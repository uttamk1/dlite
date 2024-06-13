def fib(n):
    if n<0:
        print('error')
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(fib(n) * fib(n-1))
n=10
for i in range (n):
    sum = fib(n)