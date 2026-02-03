import json

from PyQt6.QtWidgets import QFileDialog, QMessageBox

from ui import UI

from constants import DB


class Notebook(UI):
    def __init__(self, last_opened_file: str = None):
        super().__init__()
        if last_opened_file is not None:
            self.start_open(last_opened_file)


    def mark_modified(self):
        self.modified = True

    def start_open(self,  last_opened_file):
        try:
            with open(last_opened_file, "r") as f:
                self.main_field.setPlainText(f.read())
        except FileNotFoundError:
            return

        self.modified = False
        self.setWindowTitle(last_opened_file)

    def open(self):
        self.path, _ = QFileDialog.getOpenFileName()

        with open(self.path, "r") as f:
            self.main_field.setPlainText(f.read())

        self.modified = False
        self.setWindowTitle(self.path)

    def save_as(self):
        path, _ = QFileDialog.getSaveFileName()
        if not path:
            return

        self.path = path
        with open(self.path, "w") as f:
            f.write(self.main_field.toPlainText())

        self.modified = False
        self.save_last_modified_file()

    def save(self):
        if self.path is None:
            self.save_as()
            return

        with open(self.path, "w") as f:
            f.write(self.main_field.toPlainText())

        self.modified = False
        self.save_last_modified_file()

    def save_last_modified_file(self):
        if self.path is None:
            return

        with open(DB, "r+") as f:
            data = json.load(f)
            data["last_opened_file"] = self.path
            f.seek(0)
            json.dump(data, f, indent=4)

    def closeEvent(self, event):
        if self.modified:
            reply = QMessageBox.question(self,
                                         "Warning",
                                         "There are some unsaved changes. Save the file?",
                                         QMessageBox.StandardButton.Yes |
                                         QMessageBox.StandardButton.No |
                                         QMessageBox.StandardButton.Cancel)
            if reply == QMessageBox.StandardButton.Yes:
                self.save()
                event.accept()
            elif reply == QMessageBox.StandardButton.No:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()