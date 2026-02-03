from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog,
    QPushButton,
    QVBoxLayout,
    QLabel
)


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Error")

        self.label = QLabel("Error")
        self.label.setObjectName("errorLabel")

        self.ok_button = QPushButton("OK")
        self.ok_button.setObjectName("ok_button")
        self.ok_button.setFixedSize(60, 37)
        self.ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ok_button)

        layout.setAlignment(self.ok_button, Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)