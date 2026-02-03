from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QTextEdit

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.modified = False
        self.path = None

        self.main_field = QTextEdit()
        self.main_field.textChanged.connect(self.mark_modified)

        self.create_menu()

        self.setCentralWidget(self.main_field)
        self.setWindowTitle("Notebook")
        self.setMinimumSize(800, 400)

    def create_menu(self):
        self.menu = self.menuBar().addMenu("File")

        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        save_as_action = QAction("Save as", self)
        close_action = QAction("Close", self)

        open_action.triggered.connect(self.open)
        save_action.triggered.connect(self.save)
        save_as_action.triggered.connect(self.save_as)
        close_action.triggered.connect(self.close)

        self.menu.addAction(open_action)
        self.menu.addAction(save_action)
        self.menu.addAction(save_as_action)
        self.menu.addSeparator()
        self.menu.addAction(close_action)

    def mark_modified(self):
        pass
    def save(self):
        pass
    def save_as(self):
        pass
    def open(self):
        pass