print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print(f"\nHello {name.title()}! You are {age}.")

if age >= 18:
    print("You can play this game!")
    want_to_play = input("Do you want to play?")
    if want_to_play == "yes":
        print("Let's play!")
elif age >= 14:
    print("You can play under supervision!")
else:
    print("You must be at least 18 to play this game!")
