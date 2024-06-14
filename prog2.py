def love_percentage(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    # Concatenate the two names
    combined_names = name1 + name2
    
    # Calculate the number of unique characters in the combined names
    unique_chars = set(combined_names)
    
    # Calculate the love percentage
    love_percentage = (len(unique_chars) % 100)
    
    return love_percentage

# Example usage:
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

result = love_percentage(name1, name2)
print("Love percentage between", name1, "and", name2, "is:", result, "%")
