import turtle
import pandas
from scoreboard import  Scoreboard

count = 0

screen = turtle.Screen()
screen.title("U.S. States Game")

name = Scoreboard()

image = "blank_states_img.gif"
screen.addshape(image)
data = pandas.read_csv("50_states.csv")
turtle.shape(image)
game = 1
all_states = data.state.to_list()
print(all_states)
guessed_states = []
missing_states = []

while len(guessed_states) <51:
    count = len(guessed_states)
    answer_state = screen.textinput(title=f"{count}/50  Guess the State", prompt="What's another state name?")
    answer_state = answer_state.title()
    for state in all_states:
        if state == answer_state:
            guessed_states.append(state)
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto((int(state_data.x), int(state_data.y)))
            t.write(answer_state)

        else:
            missing_states.append(state)







screen.exitonclick()