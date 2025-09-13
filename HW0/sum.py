print('This program adds two numbers between 0-9. The program will only work with numeric inputs.')
x = 0
y = 0

x = input('Enter a number between 0-9:')
x = int(x)
while x < 0 or x > 9: 
    print('Invalid input, please try again.')
    x = input('Enter a number between 0-9:')
    x = int(x)

y = input('Enter another number:')
y = int(y)
while y < 0 or y > 9: 
    print('Invalid input, please try again.')
    y = input('Enter a number between 0-9:')
    y = int(y)

z = x + y
print("The sum of the two numbers is: ", z)