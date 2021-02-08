from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

# TODO 1. Add multiple choice questions.
# 1a. lay out four choices on ui
# 1b. fill choices at the same time as question. Fill answers randomly if not boolean.
# 1c. Answers are buttons, text value can be used as answer to check against correct answer.


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=40, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0/{len(self.quiz.question_list)}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # true_image = PhotoImage(file="./images/true.png")
        # false_image = PhotoImage(file="./images/false.png")
        # self.true_button = Button(image=true_image, command=self.pressed_true, highlightthickness=0)
        # self.true_button.grid(row=2, column=0)
        # self.false_button = Button(image=false_image, command=self.pressed_false, highlightthickness=0)
        # self.false_button.grid(row=2, column=1)

        # Set up Buttons
        # self.answer_1 = Button(text=self.quiz.q_text)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Some question text that gets really long",
            font=("Arial", 18, "italic"),
            width=280,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        print(f'in give_feedback {is_right}')
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
