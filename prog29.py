def word_frequency(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Create an empty dictionary to store word frequencies
    frequency = {}

    # Iterate through each word in the sentence
    for word in words:
        # Increment the count for each word in the dictionary
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Example usage
sentence = "Hello world, how are you? Hello world!"
frequency = word_frequency(sentence)
print("Frequency of each word in the sentence:")
for word, count in frequency.items():
    print(f"{word}: {count}")
