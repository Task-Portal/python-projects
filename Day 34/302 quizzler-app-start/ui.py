from tkinter import *
from tkinter import messagebox

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, questions):
        self.questions = questions
        self.score=0
        self.current_question = 0
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=50, pady=50, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, background="white")

        # self.canvas.create_image(150, 207, image=background_img)
        self.quote_text = self.canvas.create_text(150, 125, text=f"{self.questions[self.current_question].text}", width=250, font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2,pady=20)

        correct_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_img, highlightthickness=0, command=lambda: self.btn_pressed("True"))
        self.correct_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=lambda: self.btn_pressed("False"))
        self.false_button.grid(row=2, column=1)

        self.label = Label(self.window, text=f"score: {self.score}", font=("Arial", 20, "italic"), fg='white',bg=THEME_COLOR)
        self.label.grid(row=0, column=1,pady=10, padx=10)
        self.window.mainloop()

    def btn_pressed(self, value):
        answer =  self.questions[self.current_question].answer


        if answer==value:
            self.score+=1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.change_bg)
        self.label.config(text=f"score:{self.score}")
        if len(self.questions)-1>self.current_question:
            self.current_question+=1
            self.canvas.itemconfig(self.quote_text, text=f"{self.questions[self.current_question].text}")
        else:
            self.false_button.config(state="disabled")
            self.correct_button.config(state="disabled")
            messagebox.showinfo(title="Finish", message=f"There are no questions. Your score is {self.score}")


    def change_bg(self):
        self.canvas.config(bg="white")


# df = QuizInterface()