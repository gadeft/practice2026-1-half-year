import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui import UI


STYLE_PATH = "style.Qss"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()

    ui = UI()
    window.setCentralWidget(ui)

    with open(STYLE_PATH) as f:
        style = f.read()
        app.setStyleSheet(style)

    window.show()
    app.exec()