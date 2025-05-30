#  NUMBER GUESSING GAME 
# Author : Bhumi Tilwani 
# A simple number guessing game with 5 attempts 
# Language : python 3 



 # To generate a random number 
import random 

# secret number is randomly choosen between 1 and 100 
secret_number  = random.randint(1, 100)

# To count the number of attempts made by the user 
attempt = 0 

# maximum  attempt  allowed 
max_attempt = 5


# Game loop: runs until user uses all attempts
while attempt < max_attempt :
    guess = int(input("Guess a number between 1 and 100: "))
    
# Input validation : number must be in the given  range 
    if guess < 1  or guess > 100:
        print(" Please enter the number between  1 and 100 only.") 
        continue

    attempt += 1  # increase attempt count 

    # check if the guess  is correct  
    if guess == secret_number:
        print(" Congratulation!  you guess right it number ")
        break 
    elif guess < secret_number : 
        print(" Too low! Try again. ")
    else:
        print("Too high! Try again. ")


        # if the user not get answer in 5 attemps 

if guess != secret_number:
    print(" sorry, you have used all attempts.")

    print("The correct answer was: ", secret_number)

    print("!! PLAY AGAIN !!  or Exit Game ")