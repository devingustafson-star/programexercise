col1 = str(input('Enter a primary color (red, blue, or yellow): '))
col2 = str(input('Enter a primary color (red, blue, or yellow): '))

if col1 == 'red' and col2 == 'blue' or col1 == 'blue' and col2 == 'red':
    print('The secondary color is purple.')
elif col1 == 'red' and col2 == 'yellow' or col1 == 'yellow' and col2 == 'red':
    print('The secondary color is orange.')
elif col1 == 'blue' and col2 == 'yellow' or col1 == 'yellow' and col2 == 'blue':
    print('The secondary color is green.')
else:
    print('Invalid input. Please enter two primary colors (red, blue, or yellow).')