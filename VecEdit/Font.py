import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog


class Font(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Диалоговые окна')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 40)
        self.button_1.setText("Кнопка")

    def getFontSize(self, size):
        size, ok_pressed = QInputDialog.getInt(
            self, "Размер шрифта", "",
            self.size, 1, 99, 1)
        if ok_pressed:
            return size


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Font()
    ex.show()
    sys.exit(app.exec_())