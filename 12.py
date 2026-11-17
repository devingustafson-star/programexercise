
package_price = 99
package_quantity = int(input('Enter the number of packages purchased: '))
if package_quantity >= 10 and package_quantity <= 19:
    discount = 0
elif package_quantity >= 20 and package_quantity <= 49:
    discount = 0.2
elif package_quantity >= 50 and package_quantity <= 99:
    discount = 0.3
elif package_quantity >= 100:
    discount = 0.4
total_cost = package_price * package_quantity * (1 - discount)
print(f'Total cost: ${total_cost:.2f}')
