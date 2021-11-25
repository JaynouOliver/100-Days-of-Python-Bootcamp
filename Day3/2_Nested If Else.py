height = int(input("What's your height?"))
if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("What's your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you've to grow taller before you can ride this")
