from imports import *
from logic import Logic


STYLE_PATH = 'style.qss'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()

    logic = Logic()

    widget = QWidget()
    widget.setLayout(logic.grid)
    window.setCentralWidget(widget)

    with open(STYLE_PATH, "r") as file:
        style = file.read()
        app.setStyleSheet(style)

    window.show()
    app.exec()