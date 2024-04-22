#Validtion Input 
while True: 
    try: 
        age = int(input("Enter your age: "))
        if age < 0: 
            print("please enter a positive integer for age.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer")

#Age classification code below 

if age >= 40:
    print("You're over the hill.")
elif age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")
