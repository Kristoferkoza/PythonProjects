from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question 1",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        cross_image = PhotoImage(file="images/false.png")
        self.unknown_button = Button(image=cross_image, highlightthickness=0, command=self.false_pressed)
        self.unknown_button.grid(row=2, column=1)

        check_image = PhotoImage(file="images/true.png")
        self.known_button = Button(image=check_image, highlightthickness=0, command=self.true_pressed)
        self.known_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.known_button.config(state="disabled")
            self.unknown_button.config(state="disabled")
        self.canvas.config(bg="white")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





