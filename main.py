print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print(f"\nHello {name.title()}! You are {age}.")

health = 10
if age >= 18:
    print("\tYou can play this game!")
    want_to_play = input("Do you want to play? ")
    if want_to_play.lower() == "yes":
        print("\nLet's play! ")
        print(f"Your current health is {health}!")

        left_or_right = input("First choice... Left ot Right(left/right)? ")
        if left_or_right.lower() == 'right':
            ans = input(
                "Nice, you follow the path and reach a lake.. Do you swim across or go around (across/around? ")
            if ans.lower() == 'around':
                print("You went around and reached the other side of the lake")
            elif ans.lower() == 'across':
                print(
                    "\nYou managed to to get across but were bit by a fish and lost 5 health")
                health -= 5
                print(f"Your current health is {health}.")
            else:
                print("\nYou lost!")

            ans = input(
                "You notice a house and a river. Which one you go to (house/river)? ")
            if ans.lower() == 'house':
                print(
                    "You want to the house and got beaten by the owner.  You lost 5 health.")
                health -= 5
                if health <= 0:
                    print("You lost!")
                else:
                    print("\nYou have made it!")
                    print("Well Done!")
            else:
                print("\nYou fell in the river.")
                print("You lost!")
        else:
            print("\nYou fell down and lost...")

    else:
        print("Bye Bye!")
elif age >= 14:
    print("You can play under supervision!")
else:
    print("You must be at least 18 to play this game!")
