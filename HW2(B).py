user_input = input('Please enter a string: ')
if user_input.isupper():
    print('The string contains uppercase letters.')
else:
    print('The string contains lowercase letters.')
if user_input.isdigit():
    print('The string contains digits.')
else:
    print('The string contains non-digits characters.')
if user_input.isalpha():
    print('The string only contains upper and lowercase letters.')
else:
    print('The string contains non-alphabets characters.')

print('Type, type, type away.' + '\nCompile. Run. Hip hip hooray!' + '\nNo error today!')


quote = str('And now for something completely different')
quote_b = quote[:6]
quote_c = quote[-4:]
quote_d = quote[14:16]
quote_e = quote[::2]
quote_f = quote[-1::-1]
print(quote_b,quote_c,quote_d,quote_e,quote_f)

pattern1 = str(".~*'")
pattern2 = pattern1 + pattern1[::-1]
print(pattern2*5)

SMALL_BEADS = 9.20
MEDIUM_BEADS = 8.52
LARGE_BEADS = 7.98

ask_small = int(input('How many boxes of small beads do you want? '))
ask_medium = int(input('How many boxes of medium beads do you want? '))
ask_large = int(input('How many boxes of small beads do you want? '))

print('SIZE      QTY    COST PER BOX      TOTALS')
print('Small {0:7d} {1:15.2f} {2:11.2f}'.format(ask_small,SMALL_BEADS,ask_small*SMALL_BEADS))