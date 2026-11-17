num = int(input('Enter a number 0 through 36: '))
if num == 0:
    print('The number is green.')
elif num >= 1 and num <= 10:
    if num % 2 == 0:
        print('The number is black.')
    else:
        print('The number is red.')
elif num >= 11 and num <= 18:
    if num % 2 == 0:
        print('The number is red.')
    else:
        print('The number is black.')
elif num >= 19 and num <= 28:
    if num % 2 == 0:
        print('The number is black.')
    else:
        print('The number is red.')
elif num >= 29 and num <= 36:
    if num % 2 == 0:
        print('The number is red.')
    else:
        print('The number is black.')
else:
    print('Invalid input. Please enter a number between 0 and 36.')