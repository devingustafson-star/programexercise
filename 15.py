year = int(input("Enter a year: "))
if year % 100 == 0:
    leap = (year % 400 == 0)
else:
    leap = (year % 4 == 0)
if leap:
    print("In", year, "February has 29 days.")
else:
    print("In", year, "February has 28 days.")
