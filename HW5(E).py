plant_name = input('Please enter the plant name: ')
plant_type = input('Please enter the plant type: ')
plant_height = int(input('Please enter the plant height: '))
if plant_type == 'Vegetable':
    print('A',plant_name,'can be planted in the Vegetable Garden')
elif plant_type == 'Flower':
    if plant_height <= 6:
        if plant_height <= 3:
            print('A',plant_name,'can be planted in the Low or the High Garden')
        else:
            print('A',plant_name,'can be planted in the High Garden')    
    else:
        print('The height of', plant_name,'exceeds the range of height.')
elif plant_type == 'Tree': 
    print('A',plant_name,'cannot be planted in any of the garden')  
else:
    print('Sorry, the plant type is invalid')




import random
print('Welcome to the guessing game.\nYou need to guess a number from 1 to 100.')
secretNum = random.randint(1,100)
print(secretNum)
guessNum = int(input('What is your guess? '))
i = 1
while guessNum != secretNum:
    if guessNum < secretNum:
        guessNum = int(input('Guess is too low.\nWhat is your guess? '))
        i += 1
    else:
        guessNum = int(input('Guess is too high.\nWhat is your guess? '))
        i += 1        
print('Congratulations!\nYou guessed the secret number in', i ,'guesses!')



import re
quote = 'Believe you can and you\'re halfway there.'
a_index = [m.start() for m in re.finditer('a',quote) ]
for i in a_index:
    print('a found at index',i)


m = int(input('Please enter the number of rows for the multiplication table: '))
num = 1
for i in range(1, m + 1): # vertical loop
    for j in range(1, i + 1): # horizontal loop, e.g: if i = 3 then output 3 6 9 before going to print()
        print(i*j, end = '\t') 
    print() # This statement automatically prints a new line. 

# correction of the last part:
m = int(input('Please enter the number of rows for the multiplication table: '))
num = 1
for i in range(1, m + 1):
    for j in range (1, i + 1):
        # convert to str is becasue rjust is a function in string
        print(str(i*j).rjust(4), end = ' ') 
        # 4: copy from example: 2.   4. the space between. and . is 4
    print()