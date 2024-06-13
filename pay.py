x=input("Name ").lower()
y=input("Name2: ").lower()
count_t = x.count('t')+y.count('t')
count_r = x.count('r')+x.count('r')
count_u = x.count('u')+x.count('u')
count_e = x.count('e')+x.count("e")
true = count_t+count_r+count_u+count_e

count_l = x.count('l')+y.count('l')
count_o = x.count('o')+x.count('o')
count_v = x.count('v')+x.count('v')
love = count_l+count_o+count_v+count_e

percentage = (10 * true) + love
print(f"your love compatibility is {percentage}%")