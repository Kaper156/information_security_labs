import sys
from PyQt5 import QtWidgets

from RGR.gui.wrapper import Wrapper

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Wrapper()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()
