from PyQt5 import QtWidgets

from RGR.gui.window import Ui_MainWindow


class Wrapper(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
