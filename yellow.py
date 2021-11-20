import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon
from untitled import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def paintEvent(self, event):  # начинаем рисование
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('#ffff00'))
            qp.drawEllipse(self.x, self.y, self.x, self.x)
            qp.end()
        self.update()

    def run(self):
        self.do_paint = True
        self.x = randint(1, 400)
        self.y = randint(1, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
