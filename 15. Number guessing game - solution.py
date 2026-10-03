import random
print("Welcome to the number guessing game. \nWe have a number that needs to be guessed. You have 10 chances.")
print("The Secret Number is between 1 to 50.")
secret_num = random.randint(1, 50)
attempts = 10
is_guess_correct = False
while attempts > 0:
    print(f'\nyou have {attempts} attempts left.')
    user_number =(int(input("Enter your guess: ")))
    if user_number == secret_num:
        print("Congats! you guessed the Right number")
        is_guess_correct = True
        break
    else:
        if user_number < secret_num:
            print("Wrong guess please, Try Higher.") 
        else:
            print("Wrong guess please, Try Lower.")                  
    attempts -= 1
if not is_guess_correct:
    print("Bad luck! You have exhausted your all attempts.")
print(f"Secret number was {secret_num}.\n GAME OVER")