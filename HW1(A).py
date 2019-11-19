import math
a = 3**2.5
b = 2
b += 3
c = 12
c /= 4
d = 5%3
print('a = ',a,'\nb = ',b,'\nc = ',c,'\nd = ',d)


print(5-7)
print(round(3.14159,4))
print(round(186282,-2))
print(min(6,-9,-3,0))

user_input = float(input('Please enter a number:'))
print('The square root of your input is:', round(math.sqrt(user_input),2)) 
print('The base10 log of your input is:',round(math.log10(user_input),2))

z1 = 4 + 3j
z2 = 2 +2j
z3 = z1*z2
print(z3)
