length = float(input("Enter the length of the first  rectangle: "))
width = float(input("Enter the width of the first rectangle: "))
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

if length * width > length2 * width2:
    print("The first rectangle has a larger area.")
elif length * width == length2 * width2:
    print("Both rectangles have the same area.")
else:
    print("The second rectangle has a larger area.")