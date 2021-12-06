import sys, os

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QSpinBox
from PyQt5.QtWidgets import QMainWindow, QApplication

from Painter import Painter


class Form(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(100, 100)

        self.lable_symb = QLabel("Glyph:", self)
        self.lable_symb.move(300, 10)
        self.lable_symb.resize(200, 70)
        self.symb_box = QLineEdit(self)
        self.symb_box.move(300, 70)
        self.symb_box.resize(70, 70)
        self.symb_box.setMaxLength(1)
        font = self.symb_box.font()
        font.setPointSize(27)
        self.symb_box.setFont(font)

        self.lable_warn = QLabel(" ", self)
        self.lable_warn.move(20, 240)
        self.lable_warn.resize(200, 70)
        self.lable_warn.setStyleSheet("color: rgb(255, 0, 0)")

        self.button = QPushButton('DESIGN', self)
        self.button.move(140, 150)
        self.button.resize(200, 70)
        self.button.clicked.connect(self.on_click)
        font = self.button.font()
        font.setPointSize(27)
        self.button.setFont(font)

        self.lable_name = QLabel("Directory:", self)
        self.lable_name.move(20, 10)
        self.lable_name.resize(200, 70)
        self.name_box = QLineEdit(self)
        self.name_box.move(20, 70)
        self.name_box.resize(200, 70)
        font = self.name_box.font()
        font.setPointSize(20)
        self.name_box.setFont(font)

        self.gen_font_but = QPushButton('COMPARE', self)
        self.gen_font_but.move(140, 450)
        self.gen_font_but.resize(200, 70)
        self.gen_font_but.clicked.connect(self.compare)
        font = self.gen_font_but.font()
        font.setPointSize(27)
        self.gen_font_but.setFont(font)

        self.dir_lbl = QLabel('Directory to compare:', self)
        self.dir_lbl.move(300, 310)
        self.font_dir = QLineEdit(self)
        self.font_dir.move(300, 350)
        self.font_dir.resize(200, 50)

        self.dir_lbl = QLabel('Font name:', self)
        self.dir_lbl.move(20, 310)
        self.font_dir = QLineEdit(self)
        self.font_dir.move(20, 350)
        self.font_dir.resize(200, 50)

        self.lable_ne_dodelal = QLabel("CAN'T FIND GOOD SVG TO TTF PARSER", self)
        self.lable_ne_dodelal.move(20, 400)
        self.lable_ne_dodelal.resize(2000, 90)
        self.lable_ne_dodelal.setStyleSheet("color: rgb(255, 0, 0);"
                                            "font-size: 70pt;")

    def compare(self):
        pass


    def on_click(self):
        if len(self.name_box.text()) <= 1:
            self.lable_warn.setText("Please try longer style name(len > 1)")
        elif len(self.symb_box.text()) == 0:
            self.lable_warn.setText("Please choose glyph")
        else:
            self.width = 200
            self.height = 200
            self.name = self.name_box.text()
            self.close()
            self.game = Game(self.width, self.height, QColor('white'), self.name, self.symb_box.text())
            self.setCentralWidget(self.game)
            self.game.setGeometry(0, 0, 2000, 1500)
            self.game.show()


class Game(QMainWindow):

    def __init__(self, w, h, col, name, glyph):
        super().__init__()
        self.painter = Painter(w, h, col, name, glyph)
        self.painter.setGeometry(100, 100, max(200, self.width() + 20), self.height() + 20)
        self.painter.setWindowTitle(f'{name}: {glyph}')
        self.painter.show()


class Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.form = Form()
        self.form.setWindowTitle('font choose')

        self.form.setGeometry(500, 500, 700, 600)
        self.form.show()


if __name__ == '__main__':
    app = QApplication([])
    start = Start()
    sys.exit(app.exec_())
