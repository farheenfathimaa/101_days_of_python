import turtle
import pandas
states=pandas.read_csv("50_states.csv")
all_states=states.state.to_list()

screen= turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states=[]


while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"({len(guessed_states)}/50) States guessed", prompt="What's another state's name?").title()
    if answer_state=="Exit":
        # with list comprehension
        remaining_states=[s for s in all_states if s not in guessed_states]
        # without list comprehension
        # remaining_states=[]
        # for s in all_states:
        #     if s not in guessed_states:
        #         remaining_states.append(s)
        df=pandas.DataFrame(remaining_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=states[states.state==answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)


