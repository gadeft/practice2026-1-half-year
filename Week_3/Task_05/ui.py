from PyQt6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QDialogButtonBox, QHBoxLayout, QPushButton, QWidget

# import about
import about.about as about
import color_picker.color_picker as color_picker
import form.logic as logic


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notebook")
        self.setMinimumSize(300, 400)
        self.setMaximumSize(600, 800)

        self.tabs = QTabWidget(self)
        self.tabs.addTab(logic.Logic(), "Main")
        self.tabs.addTab(color_picker.ColorPicker(), "Settings")
        self.tabs.addTab(about.About(), "About")

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.tabs)
        self.setLayout(self.main_layout)


