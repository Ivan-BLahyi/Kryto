from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,
                             QMessageBox, QRadioButton)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс від Chebyrec')
question = QLabel('Коли розстріляли Адольфа')
btn_answer1 = QRadioButton('У 2024')
btn_answer2 = QRadioButton('У 1945')
btn_answer3 = QRadioButton('Я не знаю')
btn_answer4 = QRadioButton('Та він сам застрелився')
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Правильно! Bи виграли атомну бомбу')
    victory_win.exec_()

def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Ні, Bи нічого не виграли')
    victory_win.exec_()

btn_answer4.clicked.connect(show_win)
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_lose)
main_win.show()
app.exec_()



