weight = float(input('Enter the weight of the package: '))
if weight <= 2:
    shipping_cost = 1.50
elif weight <= 6 and weight > 2:
    shipping_cost = 3.00
elif weight <= 10 and weight > 6:
    shipping_cost = 4.00
else:
    shipping_cost = 4.75
print(f'Shipping cost: ${shipping_cost:.2f}')