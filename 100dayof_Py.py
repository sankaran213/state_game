import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
i = 0
data = pandas.read_csv("50_states.csv")
all__states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    state = screen.textinput(title = f" {i}/50 Count ", prompt = "What's another state's name?").title()
    if state == "Exit":
        missing_states = []
        for states in all__states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break



    if state in all__states:
        guessed_states.append(state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state)
        i += 1

