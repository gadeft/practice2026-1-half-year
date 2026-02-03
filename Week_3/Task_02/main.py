import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QStackedLayout
)


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Task 2")
window.setMinimumSize(769, 318)

btn_greet = QPushButton("Привітати")
btn_clear = QPushButton("Очистити")
btn_quit = QPushButton("Вийти")
lbl_show = QLabel("Вітаю, користувач!")
lbl_hide = QLabel()


h_layout = QHBoxLayout()
v_layout = QVBoxLayout()
s_layout = QStackedLayout()

v_layout.addWidget(btn_greet)
v_layout.addWidget(btn_clear)
v_layout.addWidget(btn_quit)

s_layout.addWidget(lbl_hide)
s_layout.addWidget(lbl_show)

h_layout.addLayout(s_layout)
h_layout.addLayout(v_layout)
widget = QWidget()
widget.setLayout(h_layout)
window.setCentralWidget(widget)


def hide():
    s_layout.setCurrentIndex(0)
def show():
    s_layout.setCurrentIndex(1)

btn_greet.clicked.connect(show)
btn_clear.clicked.connect(hide)
btn_quit.clicked.connect(app.quit)


with open("style.qss", "r") as file:
    style = file.read()
    app.setStyleSheet(style)


window.show()
app.exec()