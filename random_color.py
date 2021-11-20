import sys

from random import randint
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtWidgets


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(692, 530)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 200, 161, 81))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Окружности"))
        self.pushButton.setText(_translate("Form", "Нарисовать окружность"))


class Example(Ui_Form):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):  # начинаем рисование
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(0, 0, 0))
            qp.drawEllipse(self.x, self.y, self.x, self.x)
            qp.end()
        self.update()

    def run(self):
        self.do_paint = True
        self.x = randint(1, 400)
        self.y = randint(1, 400)

    def paintEvent(self, event):  # начинаем рисование
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(self.r, self.g, self.b))
            qp.drawEllipse(self.x, self.y, self.y, self.y)
            qp.end()
        self.update()

    def run(self):
        self.do_paint = True
        self.x = randint(1, 600)
        self.y = randint(1, 200)
        self.r = randint(0, 255)
        self.g = randint(0, 255)
        self.b = randint(0, 255)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
