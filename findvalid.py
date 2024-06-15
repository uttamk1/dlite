def findValid(exp):
    stack=[]
    for char in exp:
        if char == ')':
            countchar= 0
            PreviousCharInStack = stack.pop()
            while(PreviousCharInStack!='('):
                countchar +=1
                PreviousCharInStack = stack.pop()
            if countchar <=1:
                return True
        else:
            stack.append(char)
    else:
        return False
print(findValid("((a+b)b)"))