from PyQt6.QtWidgets import QWidget, QColorDialog, QFileDialog, QMenu
from PyQt6.QtGui import QPainter, QPen, QImage, QAction
from PyQt6.QtCore import Qt, QPoint

from ui import UI
from contants import *


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)

        self.figures = list()

        self.image = QImage(self.size(), QImage.Format.Format_RGB32)
        self.image.fill(Qt.GlobalColor.white)

        self.pen_color = Qt.GlobalColor.black
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.drawing = False
        self.mode = MODES["line"]

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)

        line = QAction("Line", self)
        circle = QAction("Circle", self)

        line.triggered.connect(lambda: self.set_mode(MODES["line"]))
        circle.triggered.connect(lambda: self.set_mode(MODES["circle"]))

        context_menu.addAction(line)
        context_menu.addAction(circle)

        context_menu.exec(event.globalPos())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)

    def mousePressEvent(self, event):
        if event.button() != Qt.MouseButton.LeftButton:
            self.drawing = False
            return

        self.drawing = True
        self.start_point = event.position().toPoint()

    def mouseReleaseEvent(self, event):
        self.drawing = False
        self.add_figure(self.start_point, self.end_point, self.mode, self.pen_color)
        self.update()

    def mouseMoveEvent(self, event):
        if not self.drawing:
            return

        self.image.fill(Qt.GlobalColor.white)
        self.end_point = event.position().toPoint()

        for i in self.figures:
            self.draw(*i)
        self.draw(self.start_point, self.end_point, self.mode, self.pen_color)

        self.update()


    def draw(self, start_point, end_point, mode, pen_color):
        painter = QPainter(self.image)
        pen = QPen(pen_color, LINE_WIDTH)
        painter.setPen(pen)

        if mode == MODES["line"]:
            painter.drawLine(start_point, end_point)
        elif mode == MODES["circle"]:
            radius = (start_point - end_point).manhattanLength()
            painter.drawEllipse(start_point, radius, radius)

    def add_figure(self, start_point, end_point, mode, pen_color):
        figure = [start_point, end_point, mode, pen_color]
        self.figures.append(figure)

    def set_mode(self, mode):
        self.mode = mode

    def clear(self):
        self.image.fill(Qt.GlobalColor.white)
        self.figures = []
        self.update()

    def save_ps(self, filename):
        self.image.save(filename, "PS")


class Logic(UI):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)

    def clear(self):
        self.canvas.clear()

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.pen_color = color

    def set_mode(self, mode):
        self.canvas.mode = mode

    def save_image(self):
        filename, _ = QFileDialog.getSaveFileName(self, filter="PostScript (*.ps)")
        if filename:
            self.canvas.save_ps(filename)