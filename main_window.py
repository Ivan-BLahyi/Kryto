from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QSpinBox,
    QGroupBox,
    QButtonGroup,
    QRadioButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
)

from PyQt5.QtCore import Qt

window = QWidget()
width, height = 500, 600

window.resize(width, height)
window.move(300, 300)
window.setWindowTitle("Memory Card")

btn_sleep = QPushButton("Відпочити")
box_minutes = QSpinBox()
box_minutes.setValue(30)

btn_menu = QPushButton("Меню")
btn_next = QPushButton("Відповісти")

RadiGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()

rbtn_1 = QRadioButton("1")
rbtn_2 = QRadioButton("2")
rbtn_3 = QRadioButton("3")
rbtn_4 = QRadioButton("4")

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadiGroupBox.setLayout(layout_ans1)

header = QHBoxLayout()
header.addWidget(btn_menu, alignment=Qt.AlignLeft)
header.addWidget(btn_sleep, alignment=Qt.AlignRight)
header.addWidget(box_minutes, alignment=Qt.AlignRight)

question = QLabel("Питання???")

main_layout = QVBoxLayout()
main_layout.addWidget(header)
main_layout.addWidget(question, alignment=Qt.AlignHCenter)
main_layout.addWidget(RadioGroupBox)
main_layout.addWidget(btn_next, stretch=2)

window.setLayout(main_layout)




