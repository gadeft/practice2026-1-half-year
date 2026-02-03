from imports import *
from ui import UI

class Logic(UI):
    def __init__(self):
        super().__init__()
        self.btn_clear.clicked.connect(self.clear)
        self.btn_save.clicked.connect(self.save)

    def clear(self):
        self.line.clear()

        self.rb_male.setChecked(False)
        self.rb_female.setChecked(False)
        self.check_agree.setChecked(False)

        self.lbl_output.hide()

    def save(self):
        if self.rb_male.isChecked():
            sex = "male"
        elif self.rb_female.isChecked():
            sex = "female"
        else:
            sex = "unknown"

        output = (f"Name: {self.line.text()}\n"
                  f"Sex: {sex}\n"
                  f"Agreed: {self.check_agree.isChecked()}")

        self.lbl_output.setText(output)
        self.lbl_output.show()


