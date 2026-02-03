from form.imports import *


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl_name = QLabel("Name")
        self.lbl_male = QLabel("Male")
        self.lbl_female = QLabel("Female")
        self.lbl_agreement = QLabel("I agree with privacy policy")
        self.lbl_output = QLabel("")
        self.lbl_output.setObjectName("output")
        self.lbl_output.hide()

        self.line = QLineEdit()

        self.btn_clear = QPushButton("Clear")
        self.btn_save = QPushButton("Save")

        self.rb_male = QRadioButton()
        self.rb_female = QRadioButton()
        self.check_agree = QCheckBox()

        self.grid = QGridLayout()
        self.grid.addWidget(self.lbl_name, 0, 0)
        self.grid.addWidget(self.line, 0, 1, 1, 3)
        self.grid.addWidget(self.lbl_male, 1, 0)
        self.grid.addWidget(self.rb_male, 1, 1)
        self.grid.addWidget(self.lbl_female, 1, 2)
        self.grid.addWidget(self.rb_female, 1, 3)
        self.grid.addWidget(self.check_agree, 2, 0)
        self.grid.addWidget(self.lbl_agreement, 2, 1, 1, 3)
        self.grid.addWidget(self.btn_clear, 3, 0, 1, 2)
        self.grid.addWidget(self.btn_save, 3, 2, 1, 2)
        self.grid.addWidget(self.lbl_output, 4, 0, 2, 4)

        self.setLayout(self.grid)
