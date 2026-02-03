from dialog import CustomDialog
from PyQt6.QtWidgets import QPushButton, QLineEdit


class AbstractButton(QPushButton):
    def __init__(self, value: str, line_field: QLineEdit):
        super().__init__(value)
        self.value = value
        self.line_field = line_field
        self.clicked.connect(self.action)

    def action(self):
        raise NotImplementedError


class DigitButton(AbstractButton):
    def action(self):
        if type(self.value) != str:
            raise TypeError("Input must be a string")
        if self.line_field.text() == "0":
            self.line_field.setText(self.value)
            return

        self.line_field.setText(self.line_field.text() + self.value)


class OperationButton(AbstractButton):
    def action(self):
        if type(self.line_field.text()) != str:
            raise TypeError("Input must be a string")

        if self.line_field.text() == "0":
            if self.value == "-":
                self.line_field.setText("-")
                return
            custom_dialog = CustomDialog()
            custom_dialog.exec()
            return

        if self.value == "-" and self.line_field.text()[-1] == "(":
            self.line_field.setText(self.line_field.text() + self.value)
            return
        elif self.line_field.text()[-1] in "/*-+(.":
            custom_dialog = CustomDialog()
            custom_dialog.exec()
            return

        self.line_field.setText(self.line_field.text() + self.value)


class DotButton(AbstractButton):
    def action(self):
        if type(self.value) != str:
            raise TypeError("Input must be a string")

        if self.line_field.text()[-1] in "0123456789":
            self.line_field.setText(self.line_field.text() + self.value)
        else:
            custom_dialog = CustomDialog()
            custom_dialog.exec()
            return


class ClearAllButton(AbstractButton):
    def action(self):
        self.line_field.setText("0")


class ClearButton(AbstractButton):
    def action(self):
        if len(self.line_field.text()) == 1:
            self.line_field.setText("0")
            return

        self.line_field.setText(self.line_field.text()[:-1])


class BracketsButton(AbstractButton):
    def action(self):
        if self.line_field.text() == "0":
            self.line_field.setText("(")
            return

        if self.line_field.text()[-1] in "/*-+(":
            self.line_field.setText(self.line_field.text() + "(")
        elif self.line_field.text()[-1] in "0123456789)":
            self.line_field.setText(self.line_field.text() + ")")
        else:
            custom_dialog = CustomDialog()
            custom_dialog.exec()


class EqualsButton(AbstractButton):
    def action(self):
        try:
            result = eval(self.line_field.text())
        except:
            custom_dialog = CustomDialog()
            custom_dialog.exec()
            return

        self.line_field.setText(str(result))