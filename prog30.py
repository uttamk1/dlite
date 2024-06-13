def reverse_words(string):
    words = string.split()  # Split the string into words
    reversed_words = words[::-1]  # Reverse the order of words
    reversed_string = ' '.join(reversed_words)  # Join the words into a string
    return reversed_string

# Example usage
original_string = "Hello world, how are you?"
reversed_string = reverse_words(original_string)
print("Original string:", original_string)
print("Reversed string (word by word):", reversed_string)
