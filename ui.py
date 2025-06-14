from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
quiz_b=QuizBrain
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas= Canvas(height=250,width=300,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.question_text=self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=('Arial',16,'italic'))



        self.photo = PhotoImage(file="images/false.png")
        self.button1=Button(image=self.photo,command=self.false_pressed)
        self.button1.grid(row=2,column=0)
        self.photo2 = PhotoImage(file="images/true.png")

        self.button2 = Button(image=self.photo2,command=self.true_pressed)
        self.button2.grid(row=2, column=1)
        self.label=Label(text=f"Score: 0",bg=THEME_COLOR,fg="white")
        self.label.grid(row=0,column=3)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.label.config(text=f"Score:{self.quiz.score}")
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz.")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)



    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)


