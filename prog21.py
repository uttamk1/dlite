# Declare variable message and assign it a string
message = "Hello, world!"
print("Length of message:", len(message))

# Concatenate two strings
string1 = "Hello"
string2 = "world"
concatenated_string = string1 + " " + string2
print("Concatenated string:", concatenated_string)

# Capitalize first letter of each word in a sentence
sentence = "this is a sample sentence"
capitalized_sentence = " ".join(word.capitalize() for word in sentence.split())
print("Capitalized sentence:", capitalized_sentence)
