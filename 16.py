answered = "no"

if answered == "no":
    print("Reboot the computer and try to connect.")
    answered = input("Did that fix the problem? ")
else:
    answered = "yes"


if answered == "no":
    print("Reboot the router and try to connect.")
    answered = input("Did that fix the problem? ")
else:
    answered = "yes"


if answered == "no":
    print("Make sure the cables between the router and modem are plugged in firmly.")
    answered = input("Did that fix the problem? ")
else:
    answered = "yes"


if answered == "no":
    print("Move the router to a new location.")
    answered = input("Did that fix the problem? ")
else:
    answered = "yes"


if answered == "yes":
    print("Glad it's fixed!")
elif answered == "no":
    print("Get a new router.")