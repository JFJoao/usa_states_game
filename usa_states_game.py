from turtle import Turtle
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Game States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_states = []

while len(correct_states) < 50:
    answer_input = screen.textinput(title=f"{len(correct_states)}/50 Guess the State", prompt="What's another State name.").title()
    screen.update()

    if answer_input == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_states: # and state != "Exit":
                missing_states.append(state)
                for missing in missing_states:
                    t = Turtle()
                    t.color("red")
                    t.hideturtle()
                    t.penup()
                    missing_state_coord = data[data.state == state]
                    t.goto(int(missing_state_coord.x), int(missing_state_coord.y))
                    t.write(state)
                backup_missing = pandas.DataFrame(missing_states)
                backup_missing.to_csv("States to learn.csv")
        break

    if answer_input in all_states:
        correct_states.append(answer_input)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_coord = data[data.state == answer_input]
        t.goto(int(state_coord.x), int(state_coord.y))
        t.write(answer_input)
        screen.update()
