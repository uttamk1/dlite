word_list = ['dad', 'mom', 'alaska', 'pen']
s1 = "qwertyuiop"
s2 ='asdfghjkl'
for word in word_list:
    contains_invalid_chars = False
    for char in word:
        if char not in s2:
            contains_invalid_chars = True
            break
    if not contains_invalid_chars:
        print(word)
    
    l = [11,'apple',12,11, 12,11,12]
    s = set(1)
    lc = []
    for i in s:
        c = l.count(i)

        lc.append(c)
    for i in lc:
        if lc.count(i)==1:
            x
