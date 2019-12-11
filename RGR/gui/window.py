# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setObjectName("toolBox")
        self.pageAlphabet = QtWidgets.QWidget()
        self.pageAlphabet.setGeometry(QtCore.QRect(0, 0, 467, 402))
        self.pageAlphabet.setObjectName("pageAlphabet")
        self.formLayout = QtWidgets.QFormLayout(self.pageAlphabet)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.pageAlphabet)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.sbAbcLength = QtWidgets.QSpinBox(self.pageAlphabet)
        self.sbAbcLength.setMinimum(1)
        self.sbAbcLength.setMaximum(2999)
        self.sbAbcLength.setObjectName("sbAbcLength")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbAbcLength)
        self.label_2 = QtWidgets.QLabel(self.pageAlphabet)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.leAbcFL = QtWidgets.QLineEdit(self.pageAlphabet)
        self.leAbcFL.setMaxLength(1)
        self.leAbcFL.setObjectName("leAbcFL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leAbcFL)
        self.label_3 = QtWidgets.QLabel(self.pageAlphabet)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.leAbcFU = QtWidgets.QLineEdit(self.pageAlphabet)
        self.leAbcFU.setMaxLength(1)
        self.leAbcFU.setObjectName("leAbcFU")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.leAbcFU)
        self.label_4 = QtWidgets.QLabel(self.pageAlphabet)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dsbAbcFrequency = QtWidgets.QDoubleSpinBox(self.pageAlphabet)
        self.dsbAbcFrequency.setDecimals(5)
        self.dsbAbcFrequency.setMaximum(1.0)
        self.dsbAbcFrequency.setObjectName("dsbAbcFrequency")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.dsbAbcFrequency)
        self.label_5 = QtWidgets.QLabel(self.pageAlphabet)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.tvAbcLettersFreqs = QtWidgets.QTableView(self.pageAlphabet)
        self.tvAbcLettersFreqs.setObjectName("tvAbcLettersFreqs")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.tvAbcLettersFreqs)
        self.label_6 = QtWidgets.QLabel(self.pageAlphabet)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAbcLoadSource = QtWidgets.QPushButton(self.pageAlphabet)
        self.btnAbcLoadSource.setObjectName("btnAbcLoadSource")
        self.horizontalLayout_2.addWidget(self.btnAbcLoadSource)
        self.leAbcSourcePath = QtWidgets.QLineEdit(self.pageAlphabet)
        self.leAbcSourcePath.setObjectName("leAbcSourcePath")
        self.horizontalLayout_2.addWidget(self.leAbcSourcePath)
        self.btnAbcCalcFreqs = QtWidgets.QPushButton(self.pageAlphabet)
        self.btnAbcCalcFreqs.setObjectName("btnAbcCalcFreqs")
        self.horizontalLayout_2.addWidget(self.btnAbcCalcFreqs)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.toolBox.addItem(self.pageAlphabet, "")
        self.pageCaesar = QtWidgets.QWidget()
        self.pageCaesar.setGeometry(QtCore.QRect(0, 0, 467, 402))
        self.pageCaesar.setObjectName("pageCaesar")
        self.formLayout_2 = QtWidgets.QFormLayout(self.pageCaesar)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.pageCaesar)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.sbCaesarKey = QtWidgets.QSpinBox(self.pageCaesar)
        self.sbCaesarKey.setObjectName("sbCaesarKey")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbCaesarKey)
        self.toolBox.addItem(self.pageCaesar, "")
        self.pageAffine = QtWidgets.QWidget()
        self.pageAffine.setObjectName("pageAffine")
        self.formLayout_3 = QtWidgets.QFormLayout(self.pageAffine)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.pageAffine)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.sbAffineB = QtWidgets.QSpinBox(self.pageAffine)
        self.sbAffineB.setObjectName("sbAffineB")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sbAffineB)
        self.sbAffineA = QtWidgets.QSpinBox(self.pageAffine)
        self.sbAffineA.setObjectName("sbAffineA")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbAffineA)
        self.label_9 = QtWidgets.QLabel(self.pageAffine)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.pageAffine)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.sbAffine_A = QtWidgets.QSpinBox(self.pageAffine)
        self.sbAffine_A.setObjectName("sbAffine_A")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbAffine_A)
        self.toolBox.addItem(self.pageAffine, "")
        self.pageViginer = QtWidgets.QWidget()
        self.pageViginer.setObjectName("pageViginer")
        self.formLayout_4 = QtWidgets.QFormLayout(self.pageViginer)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_11 = QtWidgets.QLabel(self.pageViginer)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.leViginerKey = QtWidgets.QLineEdit(self.pageViginer)
        self.leViginerKey.setObjectName("leViginerKey")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leViginerKey)
        self.toolBox.addItem(self.pageViginer, "")
        self.pageGamma = QtWidgets.QWidget()
        self.pageGamma.setObjectName("pageGamma")
        self.formLayout_5 = QtWidgets.QFormLayout(self.pageGamma)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_12 = QtWidgets.QLabel(self.pageGamma)
        self.label_12.setObjectName("label_12")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.sbGammaInitKey = QtWidgets.QSpinBox(self.pageGamma)
        self.sbGammaInitKey.setObjectName("sbGammaInitKey")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.sbGammaInitKey)
        self.sbGammaA = QtWidgets.QSpinBox(self.pageGamma)
        self.sbGammaA.setObjectName("sbGammaA")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbGammaA)
        self.sbGammaB = QtWidgets.QSpinBox(self.pageGamma)
        self.sbGammaB.setObjectName("sbGammaB")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbGammaB)
        self.label_14 = QtWidgets.QLabel(self.pageGamma)
        self.label_14.setObjectName("label_14")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_13 = QtWidgets.QLabel(self.pageGamma)
        self.label_13.setObjectName("label_13")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.sbGammaM = QtWidgets.QSpinBox(self.pageGamma)
        self.sbGammaM.setObjectName("sbGammaM")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sbGammaM)
        self.label_15 = QtWidgets.QLabel(self.pageGamma)
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.toolBox.addItem(self.pageGamma, "")
        self.pageFeistel = QtWidgets.QWidget()
        self.pageFeistel.setObjectName("pageFeistel")
        self.formLayout_6 = QtWidgets.QFormLayout(self.pageFeistel)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_16 = QtWidgets.QLabel(self.pageFeistel)
        self.label_16.setObjectName("label_16")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.sbFeistelBlockSize = QtWidgets.QSpinBox(self.pageFeistel)
        self.sbFeistelBlockSize.setMinimum(2)
        self.sbFeistelBlockSize.setMaximum(1024)
        self.sbFeistelBlockSize.setSingleStep(2)
        self.sbFeistelBlockSize.setObjectName("sbFeistelBlockSize")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbFeistelBlockSize)
        self.leFeistelEmptyChar = QtWidgets.QLineEdit(self.pageFeistel)
        self.leFeistelEmptyChar.setMaxLength(1)
        self.leFeistelEmptyChar.setObjectName("leFeistelEmptyChar")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.leFeistelEmptyChar)
        self.label_17 = QtWidgets.QLabel(self.pageFeistel)
        self.label_17.setObjectName("label_17")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.pageFeistel)
        self.label_18.setObjectName("label_18")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.sbFeistelRounds = QtWidgets.QSpinBox(self.pageFeistel)
        self.sbFeistelRounds.setMinimum(1)
        self.sbFeistelRounds.setMaximum(1024)
        self.sbFeistelRounds.setSingleStep(1)
        self.sbFeistelRounds.setObjectName("sbFeistelRounds")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sbFeistelRounds)
        self.label_19 = QtWidgets.QLabel(self.pageFeistel)
        self.label_19.setObjectName("label_19")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_19)
        self.toolBox.addItem(self.pageFeistel, "")
        self.pageFrequency = QtWidgets.QWidget()
        self.pageFrequency.setObjectName("pageFrequency")
        self.toolBox.addItem(self.pageFrequency, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSetSource = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetSource.setObjectName("btnSetSource")
        self.horizontalLayout.addWidget(self.btnSetSource)
        self.leSourcePath = QtWidgets.QLineEdit(self.centralwidget)
        self.leSourcePath.setObjectName("leSourcePath")
        self.horizontalLayout.addWidget(self.leSourcePath)
        self.btnLoadSource = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadSource.setObjectName("btnLoadSource")
        self.horizontalLayout.addWidget(self.btnLoadSource)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnCiphering = QtWidgets.QPushButton(self.centralwidget)
        self.btnCiphering.setObjectName("btnCiphering")
        self.verticalLayout.addWidget(self.btnCiphering)
        self.btnSwap = QtWidgets.QPushButton(self.centralwidget)
        self.btnSwap.setObjectName("btnSwap")
        self.verticalLayout.addWidget(self.btnSwap)
        self.btnDeciphering = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeciphering.setObjectName("btnDeciphering")
        self.verticalLayout.addWidget(self.btnDeciphering)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnSetOut = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetOut.setObjectName("btnSetOut")
        self.horizontalLayout_4.addWidget(self.btnSetOut)
        self.leOutPath = QtWidgets.QLineEdit(self.centralwidget)
        self.leOutPath.setObjectName("leOutPath")
        self.horizontalLayout_4.addWidget(self.leOutPath)
        self.btnSaveSource = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveSource.setObjectName("btnSaveSource")
        self.horizontalLayout_4.addWidget(self.btnSaveSource)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_3.addWidget(self.plainTextEdit_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.sbAbcLength, self.leAbcFL)
        MainWindow.setTabOrder(self.leAbcFL, self.leAbcFU)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Мощность:"))
        self.label_2.setText(_translate("MainWindow", "Первая прописная:"))
        self.label_3.setText(_translate("MainWindow", "Первая заглавная:"))
        self.label_4.setText(_translate("MainWindow", "Индекс совападений:"))
        self.label_5.setText(_translate("MainWindow", "Частоты букв:"))
        self.label_6.setText(_translate("MainWindow", "Автоподсчет:"))
        self.btnAbcLoadSource.setText(_translate("MainWindow", "Выбрать образец"))
        self.btnAbcCalcFreqs.setText(_translate("MainWindow", "Подсчет частот"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageAlphabet), _translate("MainWindow", "Алфавит"))
        self.label_7.setText(_translate("MainWindow", "Ключ:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageCaesar), _translate("MainWindow", "Шифр цезаря"))
        self.label_8.setText(_translate("MainWindow", "B:"))
        self.label_9.setText(_translate("MainWindow", "A:"))
        self.label_10.setText(_translate("MainWindow", "-A:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageAffine), _translate("MainWindow", "Афинный шифр"))
        self.label_11.setText(_translate("MainWindow", "Ключ:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageViginer), _translate("MainWindow", "Шифр Вижинера"))
        self.label_12.setText(_translate("MainWindow", "Нач. ключ:"))
        self.label_14.setText(_translate("MainWindow", "B:"))
        self.label_13.setText(_translate("MainWindow", "A:"))
        self.label_15.setText(_translate("MainWindow", "M:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageGamma), _translate("MainWindow", "Гамма шифр"))
        self.label_16.setText(_translate("MainWindow", "Размер блока:"))
        self.label_17.setText(_translate("MainWindow", "Дополняющий символ:"))
        self.label_18.setText(_translate("MainWindow", "Раундов шифрования:"))
        self.label_19.setText(_translate("MainWindow", "В качестве функции шифрования - Гамма шифр, настройте его"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageFeistel),
                                 _translate("MainWindow", "Блочное шифрование Фейстеля"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageFrequency), _translate("MainWindow", "Частотный анализ"))
        self.btnSetSource.setText(_translate("MainWindow", "Обзор"))
        self.btnLoadSource.setText(_translate("MainWindow", "Загрузить"))
        self.btnCiphering.setText(_translate("MainWindow", "Зашифровать >>"))
        self.btnSwap.setText(_translate("MainWindow", ">> Поменять <<"))
        self.btnDeciphering.setText(_translate("MainWindow", "<< Расшифровать"))
        self.btnSetOut.setText(_translate("MainWindow", "Обзор"))
        self.btnSaveSource.setText(_translate("MainWindow", "Сохранить"))