BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas 
import random

data=pandas.read_csv("data/french_words.csv")
to_learn=data.to_dict(orient="records")
current_card={}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_bg,image=card_front)
    flip_timer=window.after(3000,func=card_flip)
    
def add():
    list.append(current_card)
def card_flip():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_bg,image=card_back)

window=Tk()
window.title("Flashy")
window.configure(bg=BACKGROUND_COLOR,padx=50,pady=50)

flip_timer=window.after(3000,func=card_flip)

canvas=Canvas(width=800,height=526)
card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage("images/card_back.png")
card_bg=canvas.create_image(400,263,image=card_front)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image,highlightthickness=0,command=next_card)
right_button.grid(column=1,row=1)

wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)

next_card()


window.mainloop()
