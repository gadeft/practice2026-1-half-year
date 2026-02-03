import json
import sys

from PyQt6.QtWidgets import QApplication

from logic import Notebook

from constants import DB


if __name__ == "__main__":
    with open(DB, "r") as f:
        data = json.load(f)
        last_opened_file = data["last_opened_file"]

    app = QApplication(sys.argv)
    window = Notebook(last_opened_file)
    window.show()
    app.exec()