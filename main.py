from PyQt5.QtWidgets import QApplication
card_width, card_height= 600

app = QApplication([])

from main_window import *

win_card.resize(card_width,card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.show()
app.exec_()



