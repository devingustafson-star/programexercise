veg = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
gf = input("Is anyone in your party gluten-free? ")

print("Here are your restaurant choices:")

if veg == "no" and vegan == "no" and gf == "no":
    print("    Joe's Gourmet Burgers")

if vegan == "no":
    print("    Main Street Pizza Company")

print("    Corner Cafe")

if vegan == "no" and gf == "no":
    print("    Mama's Fine Italian")

print("    The Chef's Kitchen")
