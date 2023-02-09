import turtle

import pandas

screen = turtle.Screen()
screen.title("Ukraine regions")
image = "ukraine1.gif"
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#
# def get_mouse_click_coor(x,y):
#     print(f"{x},{y}")

#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# data = pandas.read_csv("50_states.csv")
data = pandas.read_csv("data.csv")
all_states = len(data)
all_state_by_title = data.state.tolist()
guessed_states = []

while True:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{all_states}Угадай город",
                                    prompt="Какое другое имя").title()

    if data[data["state"] == answer_state].empty == False:
        line = data[data["state"] == answer_state]
        t = turtle.Turtle()
        t.penup()
        t.goto(int(line.x), int(line.y))
        t.hideturtle()
        t.pendown()
        t.write(answer_state)
        guessed_states.append(answer_state)
    if len(guessed_states) == all_states or answer_state == "Exit":
        new_list=[]
        for i in all_state_by_title:
            if i not in guessed_states:
                new_list.append(i)
        to_csv=   pandas.DataFrame({
            "Missed states": new_list
        })
        to_csv.to_csv("Missed states")

        break
