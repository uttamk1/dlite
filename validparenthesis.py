s="([]())"
# # mapping = {")": "(", "}": "{", "]": "["}
# # stack=[]

# for i in s:
#     if i in mapping:
#         stack.pop() if stack else '#'

def findValid(parentheses):
    stack = []
    openbrackets = ['(','[', '{']
    for i in parentheses:
      if i in openbrackets:
        stack.append(i)
      elif i == ')' and '(' == stack[-1] :
        stack.pop()
      elif i == ']' and '[' == stack[-1] :
        stack.pop()
    return True if len(stack) == 0 else False     
print(findValid(s))


# s = "([]())))"

# def findValid(parentheses):
#     stack = []
#     openbrackets = ['(', '[', '{']
#     for char in parentheses:
#         if char in openbrackets:
#             stack.append(char)
#         elif char == ')' and (not stack or stack[-1] != '('):
#             return False
#         elif char == ']' and (not stack or stack[-1] != '['):
#             return False
#         elif char == '}' and (not stack or stack[-1] != '{'):
#             return False
#         else:
#             stack.pop()
#     return True if len(stack) == 0 else False

# print(findValid(s))
