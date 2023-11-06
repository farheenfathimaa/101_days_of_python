logo= """

   ___                                                     _               
  / _ \_   _  ___  ___ ___    __ _   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|  / _` | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\ | |_| |  __/\__ \__ \ | (_| | | | | | |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \__,_| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                           

"""    
print(logo)                                                                 
import random as r
print("Welcome to the number guessing game!")                                                                       
print("I'm thinking about number between 1 and 100")
diff=input("choose a difficulty. Type 'easy' or 'hard': ")
def game(attempts):
    """this function allows us to start the game"""
    num=r.randint(1,100)
    while attempts>0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess=int(input("Make a guess: "))
        if guess==num:
            print(f"You got it! The answer was {num}")
            break
        elif guess>num:
            print("Too high")
            attempts-=1
            if attempts>0:
                print("Guess again")
        elif guess<num:
            print("Too low")
            attempts-=1
            if attempts>0:
                print("Guess again")
    if attempts==0:
        print("You've run out of guesses, you lose")
if diff=="easy":
    attempts=10
    game(10)
elif diff=="hard":
    attempts=5
    game(5)