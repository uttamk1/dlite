find permutations of given string:
def find_permutations(s):
    # Helper function to generate permutations recursively
    def generate_permutations(current, remaining):
        if len(remaining) == 0:
            permutations.append(current)
        else:
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i+1:]
                generate_permutations(new_current, new_remaining)

    permutations = []
    generate_permutations("", s)
    return permutations

# Example usage:
if __name__ == "__main__":
    input_string = "abc"
    print(f"Permutations of '{input_string}':")
    permutations = find_permutations(input_string)
    for perm in permutations:
        print(perm)
