print("Select your ride: ")
print("1. Bike")
print("2. Car")

choice =int(input("Enter your choices: "))

if(choice == 1):
    print("What type of bike?")
    print("1.Scooty\n")
    print("Scooter\n")

    choice2 = int(input("Enter your choice 2: "))
    if choice2 == 1:
        print("You have selected scooty")
    else:
        print("You have selected scooter")

    