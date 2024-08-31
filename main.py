from PyQt5.QtWidgets import QApplication
card_width, card_height= 600

app = QApplication([])

from main_window import *

window.resize(card_width,card_height)
window.move(300, 300)
window.setWindowTitle('Memory Card')

window.show()
app.exec_()



