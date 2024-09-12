from PyQt5.QtWidgets import QApplication
import random

app = QApplication([])

from main_window import *

window.show()


class Question:
    def __init__(self, question, right_ans, ans2, ans3, ans4):
        self.question = question
        self.right_answer = right_ans
        self.wrong1 = ans2
        self.wrong2 = ans3
        self.wrong3 = ans4
        self.actual = True
        self.total = 0
        self.correct = 0

    def set_right(self):
        self.correct += 1
        self.total += 1

    def set_wrong(self):
        self.total += 1


questions = [
    Question("2 + 2=?", "4", "2", "22", "+"),
    Question("Хто синій?", "небо", "море", "ялинка", "синій"),
    Question("Питання2", "правильно?", "неправильно 1", "неправильно 2", "неправильно 3"),
    Question("Питання3", "правильно?", "неправильно 1", "неправильно 2", "неправильно 3"),
]


def display_question():
    global q
    q = random.choice(questions)

    radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    random.shuffle(radio_list)
    answer = radio_list[0]
    wrong1, wrong2, wrong3 = radio_list[1:]

    answer.setText(q.right_answer)
    wrong1.setText(q.wrong1)
    wrong2.setText(q.wrong2)
    wrong3.setText(q.wrong3)

    question.setText(q.question)


def next_question():
    rbtn_1.show()
    rbtn_2.show()
    rbtn_3.show()
    rbtn_4.show()
    btn_next.setText("Відповісти")
    RadioGroupBox.setTitle("Варіанти відповідей")
    display_question()
    btn_next.clicked.disconnect()
    btn_next.clicked.connect(set_answer)


def set_answer():
    btn = RadioGroup.checkedButton()
    btn_next.setText("Наступне питання")
    rbtn_1.hide()
    rbtn_2.hide()
    rbtn_3.hide()
    rbtn_4.hide()
    if btn.text() == q.right_answer:
        RadioGroupBox.setTitle("Правильно")
        q.set_right()
    else:
        RadioGroupBox.setTitle("Неправильно")
        q.set_wrong()
    btn_next.clicked.disconnect()
    btn_next.clicked.connect(next_question)


display_question()
btn_next.clicked.connect(set_answer)

app.exec_()




