import random as r
from hangman_words import word_list 
from hangman_art import logo,stages 
import os

print(logo)
word=r.choice(word_list)
display=[]
lives=6
for i in word:
    display+="_"
end_of_game=False
while not end_of_game:
    
    guess=input("Guess a letter: ").lower()
    os.system('cls')
    if guess in word:
        print(f"You've already guessed '{guess}'")
    for pos in range(len(word)):
        letter=word[pos]
        if letter==guess:
            display[pos]=letter
    if guess not in word:
        print(f"'{guess}' is not in the word, so you lose a life")
        lives-=1
    print(f"".join(display))
    if "_" not in display:
        end_of_game=True
        print("you won!;)")
    
    print(f"remaining lives: {lives}")
    print(stages[lives])
    if lives==0:
            print(f"You lose!:( the word was {word}")
            break