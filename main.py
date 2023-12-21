import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


num_correct_guess = 0
correct_states = data.state.to_list()
correct_states_guessed = []
states_not_guessed = []
states_not_guessed = correct_states
 
while num_correct_guess != 50:
    answer_state = screen.textinput(title=f"{num_correct_guess}/50 States Correct",prompt="What's another state's name?").title()
    state_data = data[data.state == answer_state]
    if answer_state == "Exit":
        break
    if answer_state in correct_states:
        num_correct_guess += 1
        correct_states_guessed.append(answer_state)
        states_not_guessed.remove(answer_state)
        state = turtle.Turtle()
        state.color("black")
        state.penup()
        state.hideturtle()
        state.goto(int(state_data.x.iloc[0]),int(state_data.y.iloc[0]))
        state.write(answer_state,font=("Courier", 8, "bold"))

states_not_guessed_data = pandas.DataFrame(states_not_guessed)

states_not_guessed_data.to_csv("states_to_learn.csv")
