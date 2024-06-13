x=int(input("Enter range"))


def isprime(a):
    return not any(a % i == 0 for i in range(2, a // 2))

if isprime(x):
    y=str(x)
    z=y[::-1]
    if y==z:
        print(f"{x} is a prime palindrome")
    else: print(f"{x} is prime but not a palindrome")
else:print("not a prime")