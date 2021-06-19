from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_txt = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.rightImage = PhotoImage(file="./images/true.png")
        self.rightButton = Button(image=self.rightImage, bd=0, pady=20, command=self.true_answer)
        self.rightButton.grid(row=2, column=0)
        self.wrongImage = PhotoImage(file="./images/false.png")
        self.leftButton = Button(image=self.wrongImage, bd=0, pady=20, command=self.false_answer)
        self.leftButton.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_txt, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_txt, text="You've reached the end of the quiz")
            self.rightButton.config(state="disabled")
            self.leftButton.config(state="disabled")
        self.canvas.config(bg="white")

    def true_answer(self):
        answer = self.quiz.check_answer("True")
        self.update_window(answer)

    def false_answer(self):
        answer = self.quiz.check_answer("False")
        self.update_window(answer)

    def update_window(self, answer):
        print(answer)
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
