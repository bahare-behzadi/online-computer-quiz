from tkinter import *
from quiz_brain import QuizBrain
import poplib

THEME_COLOR = "#0B666A"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_manage = quiz_brain
        self.window = Tk()
        self.window.title("Assess your knowledge")
        self.window.iconbitmap("images/icon.ico")
        self.window.config(pady=30, padx=30, bg=THEME_COLOR)

        self.score_label = Label(text=f"score: 0", bg=THEME_COLOR,
                                 foreground="white", font=("arial", 16))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=600, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        back_image = PhotoImage(file="images/back.png")
        self.canvas.create_image(300, 125, image=back_image)
        self.question_text = self.canvas.create_text(160, 100,
                                                     font=("arial", 18, "bold", "italic"),
                                                     width=280,
                                                     text="Question",
                                                     fill=THEME_COLOR)

        tic_image = PhotoImage(file="images/true.png")
        self.tic_button = Button(image=tic_image, highlightthickness=0, command=self.tic_pressed)
        self.tic_button.grid(row=2, column=1)

        cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.cross_pressed)
        self.cross_button.grid(row=2, column=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_manage.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz_manage.score}")
            self.window.config(bg=THEME_COLOR)
            question_content = self.quiz_manage.next_question()
            self.canvas.itemconfig(self.question_text, text=question_content)
        else:
            self.canvas.itemconfig(self.question_text, text="You finished the quiz!!!")

    def tic_pressed(self):
        self.give_feedback(self.quiz_manage.check_answer("True"))

    def cross_pressed(self):
        self.give_feedback(self.quiz_manage.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.window.config(bg="green")
        else:
            self.window.config(bg="red")
        self.window.after(1000, self.get_next_question)







