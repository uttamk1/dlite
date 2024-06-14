s = "a9b42b5"

l=[]
for i in s:
    if i.isdigit() and i not in l:
        l.append(i)
def is_sequential(s):
    # Convert the string to a list of integers
    digits = [int(char) for char in s if char.isdigit()]

    # Check if each consecutive pair of digits increments by 1
    for i in range(len(digits) - 1):
        if digits[i] + 1 != digits[i + 1]:
            return False
    return True
for number in l:
    if is_sequential(number):
        print(number, "forms a sequential sequence.")
    else:
        print(number, "does not form a sequential sequence.")

l.sort()
x =''.join(l)
print(x)
