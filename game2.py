import random
import time

# Define game variables
supplies = 20
equipment_health = 100
atmosphere_failure = False
alien_life_discovered = False
team_members = ["Dr. Bill Chandler", "Dr. Sarah Miller", "Engineer Mark Johnson"]
relationships = {"Dr. Bill Chandler": 50, "Dr. Sarah Miller": 50, "Engineer Mark Johnson": 50}

# Introduction
print("Welcome to Trouble on Titan - An Extended Text-Based Adventure Game!")
print("You are part of a team of scientists and engineers on a mission to establish a research base on Saturn's moon, Titan.")
print("Your goal is to survive, discover alien life, and make important decisions for the team's future.")
print("Good luck!\n")

# Main game loop
while True:
    print("\nOptions:")
    print("1. Check supplies")
    print("2. Check equipment health")
    print("3. Investigate mysterious phenomena")
    print("4. Search for alien life")
    print("5. Interact with team members")
    print("6. Make a decision")
    print("7. Quit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"You have {supplies} supplies left.")

    elif choice == '2':
        print(f"Equipment Health: {equipment_health}%")

    elif choice == '3':
        if atmosphere_failure:
            print("Your equipment malfunctions due to the thick atmosphere. You must repair it.")
            time.sleep(2)
            repair_chance = random.randint(1, 100)
            if repair_chance > 50:
                print("After some effort, you manage to fix the equipment.")
                atmosphere_failure = False
                equipment_health -= 10
            else:
                print("You struggle to repair the equipment, but it's still malfunctioning.")
                equipment_health -= 20
        else:
            print("You investigate mysterious phenomena but find nothing unusual.")

    elif choice == '4':
        if not alien_life_discovered:
            print("You search for signs of alien life.")
            time.sleep(2)
            discovery_chance = random.randint(1, 100)
            if discovery_chance > 70:
                print("You make a groundbreaking discovery: evidence of alien life!")
                alien_life_discovered = True
            else:
                print("You continue to study the environment for signs of alien life.")
        else:
            print("You continue to study the alien lifeforms.")

    elif choice == '5':
        print("You interact with your team members:")
        for member in team_members:
            print(f"{member} - Relationship: {relationships[member]}")

    elif choice == '6':
        if alien_life_discovered:
            print("You must decide whether to study the alien lifeforms or prioritize the safety of the team.")
            decision = input("What will you do? (study/safety): ").lower()
            if decision == 'study':
                print("You choose to study the alien lifeforms, advancing scientific knowledge.")
                relationships["Dr. Bill Chandler"] += 10
            elif decision == 'safety':
                print("You prioritize the safety of the team, taking precautions.")
                equipment_health += 20
            else:
                print("Invalid choice. Please choose 'study' or 'safety'.")
        else:
            print("There is no major decision to make at the moment.")

    elif choice == '7':
        print("Thanks for playing Trouble on Titan!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
    
    # Simulate the passage of time
    time.sleep(1)

    # Random events
    if random.random() < 0.1:
        atmosphere_failure = True
        print("Warning: Equipment malfunction due to the thick atmosphere!")

    supplies -= 1

    if supplies <= 0:
        print("You have run out of supplies. Game over!")
        break

    if equipment_health <= 0:
        print("Your equipment has broken down completely. Game over!")
        break
