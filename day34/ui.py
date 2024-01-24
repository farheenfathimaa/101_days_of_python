from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.score=Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score.grid(column=1,row=0)

        self.canvas=Canvas(width=300,height=250,background="white")
        self.question_text=self.canvas.create_text(
            150,
            125,
            width=280,
            text="something",
            fill=THEME_COLOR,
            font=("Arial",20,"italic")
        )
        self.canvas.grid(column=0,row=1,columnspan=2,pady=20)

        right_image=PhotoImage(file="images/true.png")
        self.right=Button(image=right_image,highlightthickness=0,command=self.true_pressed)
        self.right.grid(column=0,row=2)

        wrong_image=PhotoImage(file="images/false.png")
        self.wrong=Button(image=wrong_image,highlightthickness=0,command=self.false_pressed)
        self.wrong.grid(column=1,row=2)
        
        self.get_next_question()
        
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz!")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right: bool):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000,func=self.get_next_question)    
