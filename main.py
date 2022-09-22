import turtle
import pandas

count = 0

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
data = pandas.read_csv("50_states.csv")
turtle.shape(image)
game = 1
print(data.state)
while game:
    answer_state = screen.textinput(title=f"{count}/50  Guess the State", prompt="What's another state name?")
    answer_state = answer_state.title()
    ans = data[data["state"] == answer_state].state.to_string()
    print(ans)






screen.exitonclick()