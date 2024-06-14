'''word_list = ['apple', 'egg', 'elephant', '$$$$$$$$$', '123qwf&&']
max_length = 0
max_word = ''
for word in word_list:
    count_special = 0
    for char in word:
        if not (char.isalnum() or char.isupper()):
            count_special += 1
    print(f'Number of special characters in {word} is {count_special}')
    if len(word) > max_length:
        max_length = len(word)
        max_word = word

print(f'Longest word is {max_word} with {max_length} letters')'''


# s = "12345yeyeye23"
# n=''
# for i in s:
#     if i.isnumeric():
#         n += i
# print("number is",n)

#     .-""""""-.
#   .'          '.
#  /   O      O   \
# :                :
# |                | 
# : ',          ,' :
#  \  '-......-'  /
#   '.          .'
#     '-......-'
s = "12345yey4444444eye23"

# n = []
# i = 0

# while i < len(s):
#     if s[i].isnumeric():
#         num = s[i]
#         j = i + 1
#         while j < len(s) and s[j].isnumeric():
#             num += s[j]
#             j += 1
#         n.append(num)
#         i = j
#     else:
#         i += 1
        
# print(n)
n=''
l=[]

for i in s:
    if i.isdigit():
        n = n+i
    else:
        l.append(n)
        n=''

print(l)

def is_sequential(s):
    # Convert the string to a list of integers
    digits = [int(char) for char in s if char.isdigit()]

    # Check if each consecutive pair of digits increments by 1
    for i in range(len(digits) - 1):
        if digits[i] + 1 != digits[i + 1]:
            return False
    return True

# Example usage:
number = "12345"
if is_sequential(number):
    print(number, "forms a sequential sequence.")
else:
    print(number, "does not form a sequential sequence.")


import re

def is_valid_email(email):
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


email = "example@email.com"
if is_valid_email(email):
    print(email, "is a valid email address.")
else:
    print(email, "is not a valid email address.")
