from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

about_info = {
    "Name": "Vasya",
    "Age": 67,
    "Date": "October 21, 2020"
}

def create_info_labels(**info):
    output = list()
    for key, value in info.items():
        lbl = QLabel(f"{key}: {value}")
        output.append(lbl)
    return output


class About(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(100)

        self.info_labels = create_info_labels(**about_info)
        self.layout = QVBoxLayout()

        for i in self.info_labels:
            self.layout.addWidget(i)
        self.setLayout(self.layout)
