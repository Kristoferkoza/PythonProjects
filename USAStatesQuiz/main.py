import pandas
import turtle

screen = turtle.Screen()
screen.title("USA States Quiz")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []
correct_answers = 0

while len(guessed_states) < 50:
    if correct_answers == 0:
        answer_state = screen.textinput(title="Guess the State",
                                        prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct",
                                        prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        correct_answers += 1


