#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <string.h>

// Define game variables
int supplies = 10;
bool atmosphere_failure = false;
bool alien_life_discovered = false;

// Function to simulate sleep (in seconds)
void sleep(int seconds) {
    clock_t start = clock();
    while ((clock() - start) < seconds * CLOCKS_PER_SEC);
}

int main() {
    char choice[10];
    char decision[10];

    // Seed the random number generator
    srand(time(NULL));

    // Introduction
    printf("Welcome to Trouble on Titan - A Text-Based Adventure Game!\n");
    printf("You are part of a team of scientists and engineers on a mission to establish a research base on Saturn's moon, Titan.\n");
    printf("Your goal is to survive, discover alien life, and make important decisions for the team's future.\n");
    printf("Good luck!\n\n");

    // Main game loop
    while (1) {
        printf("\nOptions:\n");
        printf("1. Check supplies\n");
        printf("2. Investigate mysterious phenomena\n");
        printf("3. Search for alien life\n");
        printf("4. Make a decision\n");
        printf("5. Quit\n");

        printf("Enter your choice: ");
        scanf("%s", choice);

        if (strcmp(choice, "1") == 0) {
            printf("You have %d supplies left.\n", supplies);
        } 
        else if (strcmp(choice, "2") == 0) {
            if (atmosphere_failure) {
                printf("Your equipment malfunctions due to the thick atmosphere. You must repair it.\n");
                sleep(2);
                printf("After some effort, you manage to fix the equipment.\n");
                atmosphere_failure = false;
            } else {
                printf("You investigate mysterious phenomena but find nothing unusual.\n");
            }
        } 
        else if (strcmp(choice, "3") == 0) {
            if (!alien_life_discovered) {
                printf("You search for signs of alien life.\n");
                sleep(2);
                printf("You make a groundbreaking discovery: evidence of alien life!\n");
                alien_life_discovered = true;
            } else {
                printf("You continue to study the alien lifeforms.\n");
            }
        } 
        else if (strcmp(choice, "4") == 0) {
            if (alien_life_discovered) {
                printf("You must decide whether to study the alien lifeforms or prioritize the safety of the team.\n");
                printf("What will you do? (study/safety): ");
                scanf("%s", decision);

                if (strcmp(decision, "study") == 0) {
                    printf("You choose to study the alien lifeforms, advancing scientific knowledge.\n");
                } 
                else if (strcmp(decision, "safety") == 0) {
                    printf("You prioritize the safety of the team, taking precautions.\n");
                } 
                else {
                    printf("Invalid choice. Please choose 'study' or 'safety'.\n");
                }
            } else {
                printf("There is no major decision to make at the moment.\n");
            }
        } 
        else if (strcmp(choice, "5") == 0) {
            printf("Thanks for playing Trouble on Titan!\n");
            break;
        } 
        else {
            printf("Invalid choice. Please choose a valid option.\n");
        }

        // Simulate the passage of time
        sleep(1);

        // Random event: Atmosphere failure
        if ((rand() % 10) < 1) {
            atmosphere_failure = true;
            printf("Warning: Equipment malfunction due to the thick atmosphere!\n");
        }

        // Random event: Supplies consumption
        supplies--;

        // Game over if supplies run out
        if (supplies <= 0) {
            printf("You have run out of supplies. Game over!\n");
            break;
        }
    }

    return 0;
}
