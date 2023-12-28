import random
import time

# Define game variables
supplies = 10
atmosphere_failure = False
alien_life_discovered = False

# Introduction
print("Welcome to Trouble on Titan - A Text-Based Adventure Game!")
print("You are part of a team of scientists and engineers on a mission to establish a research base on Saturn's moon, Titan.")
print("Your goal is to survive, discover alien life, and make important decisions for the team's future.")
print("Good luck!\n")

# Main game loop
while True:
    print("\nOptions:")
    print("1. Check supplies")
    print("2. Investigate mysterious phenomena")
    print("3. Search for alien life")
    print("4. Make a decision")
    print("5. Quit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"You have {supplies} supplies left.")

    elif choice == '2':
        if atmosphere_failure:
            print("Your equipment malfunctions due to the thick atmosphere. You must repair it.")
            time.sleep(2)
            print("After some effort, you manage to fix the equipment.")
            atmosphere_failure = False
        else:
            print("You investigate mysterious phenomena but find nothing unusual.")

    elif choice == '3':
        if not alien_life_discovered:
            print("You search for signs of alien life.")
            time.sleep(2)
            print("You make a groundbreaking discovery: evidence of alien life!")
            alien_life_discovered = True
        else:
            print("You continue to study the alien lifeforms.")

    elif choice == '4':
        if alien_life_discovered:
            print("You must decide whether to study the alien lifeforms or prioritize the safety of the team.")
            decision = input("What will you do? (study/safety): ").lower()
            if decision == 'study':
                print("You choose to study the alien lifeforms, advancing scientific knowledge.")
            elif decision == 'safety':
                print("You prioritize the safety of the team, taking precautions.")
            else:
                print("Invalid choice. Please choose 'study' or 'safety'.")
        else:
            print("There is no major decision to make at the moment.")

    elif choice == '5':
        print("Thanks for playing Trouble on Titan!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
    
    # Simulate the passage of time
    time.sleep(1)

    # Random event: Atmosphere failure
    if random.random() < 0.1:
        atmosphere_failure = True
        print("Warning: Equipment malfunction due to the thick atmosphere!")

    # Random event: Supplies consumption
    supplies -= 1

    # Game over if supplies run out
    if supplies <= 0:
        print("You have run out of supplies. Game over!")
        break
