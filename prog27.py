def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

# Example usage
rows = 5
print_pyramid(rows)
