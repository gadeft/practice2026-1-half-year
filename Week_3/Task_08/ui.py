from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction

from contants import MODES


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graphics")

        self.menubar = self.menuBar()

        self.create_file_menu()
        self.create_edit_menu()

    def create_file_menu(self):
        file_menu = self.menuBar().addMenu("File")

        save_action = QAction("Save (.ps)", self)

        save_action.triggered.connect(self.save_image)

        file_menu.addAction(save_action)

    def create_edit_menu(self):
        edit_menu = self.menuBar().addMenu("Edit")

        line = QAction("Line", self)
        circle = QAction("Circle", self)
        color = QAction("Color", self)
        clear = QAction("Clear", self)

        line.triggered.connect(lambda: self.set_mode(MODES["line"]))
        circle.triggered.connect(lambda: self.set_mode(MODES["circle"]))
        color.triggered.connect(self.choose_color)
        clear.triggered.connect(self.clear)

        edit_menu.addAction(line)
        edit_menu.addAction(circle)
        edit_menu.addSeparator()
        edit_menu.addAction(color)
        edit_menu.addSeparator()
        edit_menu.addAction(clear)


    def clear(self):
        pass

    def choose_color(self):
        pass

    def set_mode(self, mode):
        pass

    def save_image(self):
        pass
