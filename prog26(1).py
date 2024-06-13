def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Example usage
num = 36
factors = find_factors(num)
print(f"The factors of {num} are: {factors}")

def find_prime_factors(number):
    prime_factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            prime_factors.append(divisor)
            number //= divisor
        divisor += 1
    return prime_factors

# Example usage
num = 36
prime_factors = find_prime_factors(num)
print(f"The prime factors of {num} are: {prime_factors}")
