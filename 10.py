print('Enter the amount of change to equal a dollar: ')
pennies = float(input('Enter the number of pennies: '))
nickels = float(input('Enter the number of nickels: '))
dimes = float(input('Enter the number of dimes: '))
quarters = float(input('Enter the number of quarters: '))

total = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)

if total == 1.0:
    print('Congratulations! You have exactly one dollar.')
elif total < 1.0:
    print(f'You have less than one dollar. You are short by ${1.0 - total:.2f}.')
else:
    print(f'You have more than one dollar. You have ${total - 1.0:.2f} extra.')