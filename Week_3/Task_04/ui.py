from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QGridLayout, QWidget

from buttons import *
from constants import *


def create_line_field() -> QLineEdit:
    # Creating, start text and alignment
    line_field = QLineEdit()
    line_field.setText("0")
    line_field.setAlignment(Qt.AlignmentFlag.AlignRight)

    # Setting validator for accepting only allowed values
    regex = QRegularExpression(r"[0-9./*\-+()]*")
    validator = QRegularExpressionValidator(regex)
    line_field.setValidator(validator)

    return line_field

def create_buttons_list(line_field: QLineEdit) -> list[AbstractButton]:
    buttons_list = []

    for button in BUTTONS:
        if button in DIGITS:
            btn = DigitButton(button, line_field)
            btn.setObjectName("num")
            buttons_list.append(btn)
        elif button in OPERATORS:
            buttons_list.append(OperationButton(button, line_field))
        elif button in DOT:
            btn = DotButton(button, line_field)
            btn.setObjectName("num")
            buttons_list.append(btn)
        elif button in CLEAR:
            buttons_list.append(ClearButton(button, line_field))
        elif button in CLEARALL:
            buttons_list.append(ClearAllButton(button, line_field))
        elif button in BRACKETS:
            buttons_list.append(BracketsButton(button, line_field))
        elif button in EQUALS:
            buttons_list.append(EqualsButton(button, line_field))
        else:
            raise Exception("Invalid button")

    return buttons_list

def create_grid_layout(line_field: QLineEdit, *buttons: AbstractButton) -> QGridLayout:
    layout = QGridLayout()
    layout.setSpacing(0)
    layout.addWidget(line_field, 0, 0, 1, 4)

    for i in range(1, int(len(buttons) / 4) + 1):
        j = 0
        while j < 4:
            try:
                btn = buttons[(i - 1) * 4 + j]
            except IndexError:
                break

            if btn.value == "0":
                layout.addWidget(btn, i, j, 1, 2)
                j += 2
                continue
            layout.addWidget(btn, i, j)
            j += 1

    return layout


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.line_field = create_line_field()
        self.buttons = create_buttons_list(self.line_field)
        self.grid = create_grid_layout(self.line_field, *self.buttons)

        self.setLayout(self.grid)