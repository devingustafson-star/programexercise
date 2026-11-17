age = int(input('Enter your age: '))
if age < 0:
    print('Invalid input. Age cannot be negative.')
elif age < 1 and age > 0:
    print('You are an infant.')
elif age < 13:
    print('You are a child.')
elif age < 20:
    print('You are a teenager.')
else:
    print('You are an adult.')