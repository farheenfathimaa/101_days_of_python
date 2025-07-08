from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    timer_name.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    ticks.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_count():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps % 8 == 0:
        # if it's 8th rep
        count_down(long_break_sec)
        timer_name.config(text="Break!",fg=RED)
    elif reps%2==0:
        # if it's 2nd/4th/6th rep
        count_down(short_break_sec)
        timer_name.config(text="Break!",fg=PINK)
    else:
        # if it's 1st/3rd/5th/7th rep
        count_down(work_sec)
        timer_name.config(text="Work",fg=GREEN)
        
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0 or count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min==0 or count_min<10:
        count_min=f"0{count_min}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_count()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✔"
        ticks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

timer_name=Label(text="Timer",font=(FONT_NAME,40,"bold"),bg=YELLOW,highlightthickness=0,fg=GREEN)
timer_name.grid(column=1,row=0)

start=Button(text="Start",font=(FONT_NAME),command=start_count)
start.grid(column=0,row=2)

reset=Button(text="Reset",font=(FONT_NAME),command=reset)
reset.grid(column=2,row=2)

ticks=Label(font=(FONT_NAME,20,"bold"),bg=YELLOW,highlightthickness=0,fg=GREEN)
ticks.grid(column=1,row=3)

window.mainloop()