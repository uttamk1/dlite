def sort_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Sort the words alphabetically
    sorted_words = sorted(words)

    # Join the sorted words back into a sentence
    sorted_sentence = ' '.join(sorted_words)

    return sorted_sentence

# Example usage
sentence = "Hello world, how are you? I am fine, thank you!"
sorted_sentence = sort_words(sentence)
print("Sorted words in the sentence:")
print(sorted_sentence)
