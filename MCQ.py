#Import tkinter and Json Library

import tkinter as tk
from tkinter import messagebox as mb
import json


#main Window

root = tk.Tk()
root.title("MCQ QUIZ")
root.geometry("800x450")
root.resizable(False, False)


#created Class name Quiz
class Quiz:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = tk.IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.datasize = len(question)
        self.correct = 0


    #display_result function for Display Result after completed the Quiz.
    def display_result(self):
        print(self.correct)
        wrong_count = self.datasize - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"wrong: {wrong_count}"
        score = int(self.correct/self.datasize*100)
        result = f"Score {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    # Chcek_ans function for check the ans correct or not.
    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True


    #Next_btn function for click next and jump next Question.
    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no == self.datasize:
            self.display_result()
            root.destroy()
        else:
            self.display_question()
            self.display_options()

    #buttons function for display next and Quit Button.
    def buttons(self):
        next_buttons = tk.Button(root, text="Next", command = self.next_btn, width=10, bg="black", fg="white", font=("arial", 16, "bold"))
        next_buttons.place(x=350, y=380)
        quit_buttons = tk.Button(root, text="Quit", command=root.destroy, width=5, bg="black", fg="white", font=("arial", 16, "bold"))
        quit_buttons.place(x=700, y=50)

    #display_function for display all question one by one.
    def display_question(self):
        q_no = tk.Label(root, text=question[self.q_no], width=68, font=("arial", 16, "bold"), anchor="w")
        q_no.place(x=70, y=100)

    #display_title function show title of quiz of upper side
    def display_title(self):
        title = tk.Label(text="MCQ Quiz", width=50, bg="green", fg="red", font=("arial", 20, "bold"))
        title.place(x=0, y=2)

    # display_options function display the all the four options
    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]["text"] = option
            val += 1

    # radio_buttons for select the one and only options which do you think is correct.
    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(root, text="", variable=self.opt_selected, value=len(q_list)+1, font=("arial", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=180, y=y_pos)
            y_pos += 40
        return q_list


# data.json is json file. read data form data.json.
with open("data.json", "r") as f:
    data = json.load(f)

question = (data["question"])
answer = (data["answer"])
options = (data["options"])

#quiz is object of Quiz() class.
quiz = Quiz()


root.mainloop()
