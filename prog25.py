def decimal_to_binary(decimal_num):
    return bin(decimal_num)

def decimal_to_octal(decimal_num):
    return oct(decimal_num)

def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num)

# Example usage
decimal_num = 424
binary_num = decimal_to_binary(decimal_num)
octal_num = decimal_to_octal(decimal_num)
hexadecimal_num = decimal_to_hexadecimal(decimal_num)

print(f"Decimal {decimal_num} in binary: {binary_num}")
print(f"Decimal {decimal_num} in octal: {octal_num}")
print(f"Decimal {decimal_num} in hexadecimal: {hexadecimal_num}")
