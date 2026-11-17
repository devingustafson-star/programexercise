month =int(input('Enter the month in numerical form: '))
day =int(input('Enter the day in numerical form: '))
year =int(input('Enter the year in numerical form (last two digits): '))

if day * month == year:
    print('The date is magic!')
else:
    print('The date is not magic.')
