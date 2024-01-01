from turtle import Turtle
ALIGN="center"
FONT=("Courier",16,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt",mode="r") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_score()