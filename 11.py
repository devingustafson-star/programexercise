book = int(input('Enter the number of books purchased this month: '))
if book == 0:
    print('You have earned 0 points.')
elif book == 2:
    print('You have earned 5 points.')
elif book == 4:
    print('You have earned 15 points.')
elif book == 6:
    print('You have earned 30 points.')
elif book >= 8:
    print('You have earned 60 points.')
else: 
    print('You have earned 0 points.')