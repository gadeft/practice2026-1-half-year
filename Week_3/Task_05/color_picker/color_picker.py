from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QColorDialog, QLabel, QMainWindow
)
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

import json

DB = "C:\\Users\\SuperDuperMegaPC\\PycharmProjects\\practice2026-1-half-year\\Week_3\\Task_05\\db.json"


class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()
        with open(DB, "r") as f:
            data = json.load(f)
            color = data["color"]
        self.color = QColor(color)

        self.button = QPushButton("Choose color")
        self.button.clicked.connect(self.choose_color)

        self.preview = QLabel()
        self.preview.setFixedSize(100, 50)
        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_preview()

        layout = QVBoxLayout()
        layout.addWidget(self.preview, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def choose_color(self):
        color = QColorDialog.getColor(self.color, self, "Choose color")
        if color.isValid():
            self.color = color
            self.update_preview()
            self.save_color()

    def update_preview(self):
        self.preview.setStyleSheet(
            f"background-color: {self.color.name()};"
            "border: 1px solid black;"
        )
        self.preview.setText(self.color.name())

    def save_color(self):
        with open(DB, "r+") as f:
            data = json.load(f)
            data["color"] = self.color.name()

            f.seek(0)

            json.dump(data, f, indent=4)