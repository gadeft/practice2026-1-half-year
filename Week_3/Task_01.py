"""
Завдання 1. Створити програму, яка відкриває вікно з фіксованими розмірами
1024х768, заголовком «Перша програма», написом «Hello, world!» та має
завершувати свою роботу після натискання кнопки «Закрити».
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QPushButton
)

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Перша програма")
window.setFixedSize(1024, 768)

lbl = QLabel("Hellow, world")
lbl.setStyleSheet("""
    font-size: 52px;
    font-family: arial, sans-serif;
    font-weight: bold;
    font-style: italic;
    background-color: rgb(0, 125, 255);
    color: rgb(0, 0, 0);
    padding-left: 300px;
""")
btn_quit = QPushButton("Quit")
btn_quit.setStyleSheet("""
    font-size: 32px;
    font-family: arial, sans-serif;
    background-color: rgb(0, 125, 255);
""")

btn_quit.clicked.connect(app.quit)

layout = QVBoxLayout()
layout.addWidget(lbl)
layout.addWidget(btn_quit)
widget = QWidget()
widget.setLayout(layout)
window.setCentralWidget(widget)

window.show()
app.exec()