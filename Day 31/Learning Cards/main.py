import os
import random
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
timer_text = ""
number = 0
count_num = 3
timer = None,
timer_text_lang = ""
word_with_translation = ""
learn_words = None


def arrow():
    global timer_text, timer_text_lang, count_num
    canvas.delete(timer_text, timer_text_lang)
    get_words()
    count_num = 3
    canvas.itemconfig(bg, image=front)
    count_down()

    if not os.path.exists("word_I_know.csv"):
        df = pd.DataFrame(columns=["English", "Russian"])
        df.to_csv("word_I_know.csv", index=False)

    output_path = 'word_I_know.csv'
    df = pd.DataFrame([word_with_translation])
    df.to_csv(output_path, index=False, mode="a", header=False)


def cross():
    global timer_text, timer_text_lang, count_num, word_with_translation
    canvas.delete(timer_text, timer_text_lang)

    if not os.path.exists("word_to_learn.csv"):
        df = pd.DataFrame(columns=["English", "Russian"])
        df.to_csv("word_to_learn.csv", index=False)

    output_path = 'word_to_learn.csv'
    df = pd.DataFrame([word_with_translation])
    df.to_csv(output_path, index=False, mode="a", header=False)

    get_words()
    count_num = 3
    canvas.itemconfig(bg, image=front)
    count_down()


def get_words():
    global timer_text, timer_text_lang, number, word_with_translation, learn_words
    if  len(learn_words)>0:
        
        number = random.randint(1, len(learn_words)-1)
    else:
        data = pd.read_csv("words.csv")
        number = random.randint(1, 2994)

    word_with_translation = {"English": data['English'][number], "Russian": data['Russian'][number]}
    # word_with_translation =f" {data['English'][number]},  {data['Russian'][number]}"

    text = (data["English"][number])
    timer_text_lang = canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"))
    timer_text = canvas.create_text(400, 263, text=text, font=("Arial", 60, "bold"))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ UI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")

bg = canvas.create_image(405, 270, image=front)
canvas.grid(row=0, column=0, columnspan=2)
right = PhotoImage(file="./images/right.png")
button_ri = Button(image=right, highlightthickness=0, command=arrow)
button_ri.grid(row=1, column=1)

wrong = PhotoImage(file="./images/wrong.png")
button_wr = Button(image=wrong, highlightthickness=0, command=cross)
button_wr.grid(row=1, column=0)

if os.path.exists("word_to_learn.csv"):
    learn_words= pd.read_csv("word_to_learn.csv").to_dict()


get_words()


# ~~~~~~~~~~~~~~~~~~~~~~~~~ Show words ~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def count_down():
    global timer_text, timer_text_lang, bg, count_num, timer, canvas

    if count_num > 0:

        print(count_num)
        count_num -= 1
        timer = window.after(1000, count_down)
    else:
        window.after_cancel(timer)
        canvas.delete(timer_text, timer_text_lang)
        canvas.itemconfig(bg, image=back)
        timer_text_lang = canvas.create_text(400, 150, text="Russian", font=("Arial", 40, "italic"), fill="white")
        data = pd.read_csv("words.csv")
        text = (data["Russian"][number])
        timer_text = canvas.create_text(400, 263, text=text, font=("Arial", 60, "bold"), fill="white")


count_down()

window.mainloop()
