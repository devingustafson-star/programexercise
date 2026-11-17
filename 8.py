people = int(input('Enter the number of people attending the cookout: '))
dogsgiven = int(input('Enter the number of hot dogs given to each person: '))

hotdogs = (people * dogsgiven) / 10
hotdogbuns = (people * dogsgiven) / 8
leftoverhotdogs = (people * dogsgiven) % 10
leftoverhotdogbuns = (people * dogsgiven) % 8

print(f'The minimum amount of hot dog packages needed is {int(hotdogs)}.')
print(f'The minimum amount of hot dog bun packages needed is {int(hotdogbuns)}.')
print(f'The leftover hot dogs are {int(leftoverhotdogs)}.')
print(f'The leftover hot dog buns are {int(leftoverhotdogbuns)}.')
