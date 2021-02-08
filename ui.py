from tkinter import *
from quiz_brain import QuizBrain
from random import shuffle
import html

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=40, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0/{len(self.quiz.question_list)}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.button_1 = Button(text="This is some long text that should wrap",
                               width=15,
                               bg=THEME_COLOR,
                               fg="white",
                               activeforeground="yellow",
                               activebackground="teal",
                               relief="groove",
                               wraplength="70 p",
                               command=self.pressed_1,
                               )
        self.button_2 = Button(text="Item 2",
                               width=15,
                               bg=THEME_COLOR,
                               fg="white",
                               activeforeground="yellow",
                               activebackground="teal",
                               relief="groove",
                               wraplength="70 p",
                               command=self.pressed_2,
                               )
        self.button_3 = Button(text="Item 3",
                               width=15,
                               bg=THEME_COLOR,
                               fg="white",
                               activeforeground="yellow",
                               activebackground="teal",
                               relief="groove",
                               wraplength="70 p",
                               command=self.pressed_3,
                               )
        self.button_4 = Button(text="Item 4",
                               width=15,
                               bg=THEME_COLOR,
                               fg="white",
                               activeforeground="yellow",
                               activebackground="teal",
                               relief="groove",
                               wraplength="70 p",
                               command=self.pressed_4,
                               )
        self.button_1.grid(row=2, column=0, pady=10)
        self.button_2.grid(row=2, column=1, pady=10)
        self.button_3.grid(row=3, column=0, pady=10)
        self.button_4.grid(row=3, column=1, pady=10)

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
        self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.answers = self.quiz.answers
            if len(self.answers) == 1:  # type is true/false
                self.answers=["True", "False"]
                self.button_1.config(text="True")
                self.button_2.config(text="False")
                self.button_3.config(text="", state="disabled")
                self.button_4.config(text="", state="disabled")
            else:
                self.answers.append(self.quiz.current_question.answer)
                self.randomize_answers()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.button_1.config(state="disabled")
            self.button_2.config(state="disabled")
            self.button_3.config(state="disabled")
            self.button_4.config(state="disabled")

    def randomize_answers(self):
        shuffle(self.answers)
        self.button_1.config(text=html.unescape(self.answers[0]))
        self.button_2.config(text=html.unescape(self.answers[1]))
        self.button_3.config(text=html.unescape(self.answers[2]), state="normal")
        self.button_4.config(text=html.unescape(self.answers[3]), state="normal")

    def pressed_1(self):
        self.give_feedback(self.quiz.check_answer(self.button_1['text']))

    def pressed_2(self):
        self.give_feedback(self.quiz.check_answer(self.button_2['text']))

    def pressed_3(self):
        self.give_feedback(self.quiz.check_answer(self.button_3['text']))

    def pressed_4(self):
        self.give_feedback(self.quiz.check_answer(self.button_4['text']))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
