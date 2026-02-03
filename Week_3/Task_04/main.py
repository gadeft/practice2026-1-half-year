import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from ui import UI
from constants import STYLE_PATH


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = UI()

    window.setCentralWidget(ui)

    with open(STYLE_PATH, 'r') as file:
        style = file.read()
        app.setStyleSheet(style)

    window.show()
    app.exec()