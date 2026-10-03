'''
Write a program to simulate role of a die/dice
a dice has 6 faces number 1 to 6 written on them
the program should randomly prints a number between 1 to 6.
'''

import random
print("Welcome to The Dice Rolling Game.")
while True:
    choice = input("Please, Press the 'Enter' to Role the dice or 'q' for quit The Game: ")
    choice = choice.strip()
    if choice == 'q':
        print("Thank you for plying the Game, Bye!!!")
        break
    elif choice == '':
        number = random.randint(1,6)
        print(f"Thank you for Rolling the Dice.\nYour dice number is: {number}")
    else:
        print("invalid input!! Please, Try again ")
print("GAME OVER!!!")        
