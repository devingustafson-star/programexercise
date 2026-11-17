mass = float(input('Enter the objects mass in kilograms: '))
weight = mass * 9.81
if weight > 500:
    print('The object is too heavy.')
elif weight < 100:
    print('The object is too light.')
print(f'The weight of the object is {weight} Newtons.')

