def find_divisible_numbers(numbers, divisor):
    divisible_numbers = [num for num in numbers if num % divisor == 0]
    return divisible_numbers

# Example usage
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
divisor = 3
divisible_numbers = find_divisible_numbers(numbers, divisor)
print(f"Numbers divisible by {divisor}: {divisible_numbers}")
