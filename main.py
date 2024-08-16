from random import  randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Визначник переможців')
button = QPushButton('Згенерувати')
text = QLabel('Натисни , щоб дізнатися переможця')
winner = QLabel('?')

