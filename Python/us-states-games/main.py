import pandas
import turtle

state = turtle.Turtle()
state.hideturtle()
state.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_on = True
data = pandas.read_csv("50_states.csv")
while game_on:
    answer_state = screen.textinput(title= "Guess the State", prompt= "What's another state's name?:")
    print(answer_state)
    list_states = data["state"].to_list()
    print(list_states)
    if answer_state.capitalize() in list_states:
        print("lo encontro")
        print(data[data["state"] == answer_state.capitalize()])
        temp = data[data["state"] == answer_state.capitalize()]
        print(temp.x)
        print(temp.y)
        state.setposition(int(temp.x), int(temp.y))
        state.write(temp["state"].item())
    else:
        print("te jodiste")

turtle.mainloop()
