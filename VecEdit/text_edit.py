import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QWidget, QPushButton, \
    QSpinBox, QComboBox, QVBoxLayout, QLabel

from get_name_ttf import font_name

from Main import Start


class TextEditor(QMainWindow):
    def __init__(self):
        super(TextEditor, self).__init__()

        self.setWindowTitle('Редактор')
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

        self.fontSize = 10

        self.text_edit.setFontPointSize(self.fontSize)

        self.fonts = []

        self.curr_font = None

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        self.menuBar.addAction("Настроить шрифт", self.setFontAction)

        fileMenu.addAction("Открыть", self.action_clicked)
        fileMenu.addAction("Сохранить", self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == 'Открыть':
            fname = QFileDialog.getOpenFileName(self)[0]

            # f = open(fname, 'wr')
            try:
                with open(fname, 'r') as f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
                print("Такого файла нет")

        if action.text() == 'Сохранить':
            fname = QFileDialog.getSaveFileName(self)[0]

            with open(fname, 'w+') as f:
                f.write(self.text_edit.toPlainText())

    def setFontAction(self):
        form = Form(self)
        form.setFocus()
        form.setWindowTitle('Settings')

        vbox = QVBoxLayout()
        vbox.addWidget(form)
        self.setLayout(vbox)

        form.setGeometry(500, 500, 700, 600)
        form.show()

        if self.curr_font:
            self.text_edit.setFont(self.curr_font)
        self.text_edit.setFontPointSize(self.fontSize)


class Form(QWidget):
    def __init__(self, p):
        super().__init__()

        self.p = p

        self.resize(100, 100)
        self.size_lbl = QLabel('Size', self)
        self.size_lbl.move(230, 70)
        self.size_lbl.resize(200, 100)

        self.size_button = QSpinBox(self)
        self.size_button.move(230, 140)
        self.size_button.resize(100, 70)
        self.size_button.setMinimum(1)
        self.size_button.setMaximum(100)
        self.size_button.valueChanged.connect(self.spinboxChanged)

        self.font_style = QComboBox(self)
        self.font_style.resize(200, 40)
        self.font_style.move(40, 40)
        self.font_style.addItems(self.p.fonts)
        self.font_style.activated[str].connect(self.changeFont)

        self.new_font_button = QPushButton(self)
        self.new_font_button.move(40, 140)
        self.new_font_button.resize(100, 70)
        self.new_font_button.setText("Добавить шрифт")
        self.new_font_button.clicked.connect(self.addFont)

        self.button = QPushButton('OK', self)
        self.button.move(40, 250)
        self.button.resize(200, 70)
        self.button.clicked.connect(self.on_click)

        self.button = QPushButton('Создать шрифт', self)
        self.button.move(40, 350)
        self.button.resize(200, 70)
        self.button.clicked.connect(self.draw)

    def draw(self):
        start = Start()

        vbox = QVBoxLayout()
        vbox.addWidget(start)
        self.setLayout(vbox)

    def on_click(self):
        self.close()

    def changeFont(self, font):
        if font:
            print(font, self.p.fontSize)
            print(font_name(font))
            print(font_name(font)['name'], self.p.fontSize)
            self.p.curr_font = QFont(font_name(font)['name'], self.p.fontSize)

    def spinboxChanged(self, value):
        self.p.fontSize = value

    def addFont(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать шрифт', '', 'Шрифт (*.ttf)')[0]
        self.font_style.addItem(fname)
        self.p.fonts.append(fname)
        QFontDatabase.addApplicationFont(fname)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()

    window.show()

    sys.exit(app.exec_())
