import os
from random import randint

from PyQt5 import QtWidgets

from RGR.gui.window import Ui_MainWindow
from ciphers.affine import AffineCipher
from ciphers.caesar import CaesarCipher
from ciphers.feistel import FeistelCipher
from ciphers.gamma import GammaCipher
from ciphers.viginer import ViginerCipher
from core.alphabet import load_english
from core.frequency import FrequencyAnalysis
from core.settings_default import get_big_text, get_small_text
from gui.threading.cipher import CipherThread
from gui.threading.frequency import FrequencyThread


class Wrapper(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.encoding = 'utf-8'

        # Init abc and ciphers
        self.abc = load_english()
        self.ciphers = {
            "caesar": CaesarCipher(self.abc, {
                'key': randint(1, self.abc.length)
            }),
            "affine": AffineCipher(self.abc, {
                'A': 3,
                'B': 4,
                '-A': 9
            }),
            "viginer": ViginerCipher(self.abc, {
                'key': 'coDeWord'
            }),
            "gamma": GammaCipher(self.abc, {
                'A': randint(1000, 4000),
                'B': randint(250, 1000),
                'M': 4096,
                'key': randint(1, 4096)
            }),

            "feistel": FeistelCipher(self.abc, {
                "block_size": 64,
                "empty_char": '#',
                "rounds": 5,
                "is_unsafe_ok": True,

                'A': randint(1000, 4000),
                'B': randint(250, 1000),
                'M': 4096,
                'key': randint(1, 4096),
            }),
        }
        # Set current cipher
        self.current_cipher = self.ciphers['caesar']
        self.cur_thread = None

        self.connect_gui()

    def set_cipher(self, key):
        self.current_cipher = self.ciphers.get(key, None)

    def load_input_text(self):
        if self.leSourcePath.text().strip():
            with open(self.leSourcePath.text(), 'rt', encoding=self.encoding) as f:
                self.ptInputText.setPlainText(f.read())

    def save_out_text(self):
        if self.leOutPath.text().strip():
            with open(self.leOutPath.text(), 'wt', encoding=self.encoding) as f:
                f.write(self.ptOutText.toPlainText())

    def select_file_diag(self, line_edit: QtWidgets.QLineEdit, callback=None, caption=None, open_mode=True):
        diag = None
        if open_mode:
            diag = QtWidgets.QFileDialog.getOpenFileName
        else:
            diag = QtWidgets.QFileDialog.getSaveFileName
            caption = caption or "Сохранение файла"

        f_path, _ = diag(self, caption or 'Выбор файла',
                         os.path.curdir)
        if f_path:
            line_edit.setText(f_path)
            if callback:
                callback()

    def show_thread_state(self, msg: str):
        self.statusbar.showMessage(msg)

    def cipher_text(self):
        text = self.ptInputText.toPlainText()
        if self.cur_thread and self.cur_thread.isRunning():
            return
        self.cur_thread = CipherThread(self.current_cipher, text, is_cipher=True)
        self.cur_thread.state.connect(self.show_thread_state)
        self.cur_thread.output.connect(self.set_output_text)
        self.cur_thread.start()

    def decipher_text(self):
        text = self.ptOutText.toPlainText()
        if self.cur_thread and self.cur_thread.isRunning():
            return
        self.cur_thread = CipherThread(self.current_cipher, text, is_cipher=False)
        self.cur_thread.state.connect(self.show_thread_state)
        self.cur_thread.output.connect(self.set_input_text)
        self.cur_thread.start()

    def set_output_text(self, text, clear=True):
        if clear and self.cbClearText.isChecked():
            self.ptInputText.setPlainText('')
        self.ptOutText.setPlainText(text)

    def set_input_text(self, text, clear=True):
        if clear and self.cbClearText.isChecked():
            self.ptOutText.setPlainText('')
        self.ptInputText.setPlainText(text)

    def swap_text(self):
        temp = self.ptInputText.toPlainText()
        self.ptInputText.setPlainText(self.ptOutText.toPlainText())
        self.ptOutText.setPlainText(temp)

    def connect_gui(self):
        # Init signals for in/out texts buttons
        self.btnLoadSource.clicked.connect(self.load_input_text)
        self.btnSaveSource.clicked.connect(self.save_out_text)
        self.btnSetSource.clicked.connect(lambda: self.select_file_diag(
            self.leSourcePath, callback=self.btnLoadSource.click, caption="Выберите исходный текст"))
        self.btnSetOut.clicked.connect(lambda: self.select_file_diag(
            self.leOutPath, caption="Укажите выходной файл", open_mode=False))

        # Init input text
        self.leSourcePath.setText(get_small_text())
        self.btnLoadSource.click()  # Load it to PlainEdit

        # Init cipher/decipher btns
        self.btnCiphering.clicked.connect(self.cipher_text)
        self.btnDeciphering.clicked.connect(self.decipher_text)
        self.btnSwap.clicked.connect(self.swap_text)
        self.btnFreqAnalysis.clicked.connect(self.do_freq_analysis)

        # Init ciphers switch
        self.cmbCurCipher.currentIndexChanged.connect(lambda: self.set_cipher(self.cmbCurCipher.currentData()))
        self.load_ciphers_to_cmb_cur_cipher()
        self.connect_toolbox()

        # Init freqs
        self.leAbcSourcePath.setText(get_big_text())
        self.load_abc_freqs()

    def connect_toolbox(self):
        # Load values from ciphers, abc, freq
        self.load_toolbox_values()

        # Abc buttons
        self.btnAbcLoadSource.clicked.connect(
            lambda: self.select_file_diag(self.leAbcSourcePath, callback=self.load_abc_freqs,
                                          caption="Выбор образца с типичным распределением частот"))

        # Set feedback for Abc page
        self.sbAbcLength.editingFinished.connect(lambda: self.abc.set_length(self.sbAbcLength.value()))
        self.leAbcFL.editingFinished.connect(lambda: self.abc.set_fl(self.leAbcFL.text()))
        self.leAbcFU.editingFinished.connect(lambda: self.abc.set_fu(self.leAbcFU.text()))
        self.dsbAbcFrequency.editingFinished.connect(
            lambda: self.abc.set_index_coincidence(self.dsbAbcFrequency.value()))
        self.sbFreqKeyFrom.editingFinished.connect(self._freq_key_from_changed_)
        self.sbFreqKeyTo.editingFinished.connect(self._freq_key_to_changed_)

        # To update freqs
        self.sbAbcLength.editingFinished.connect(self.update_abc_freqs)
        self.leAbcFL.editingFinished.connect(self.update_abc_freqs)
        self.leAbcFU.editingFinished.connect(self.update_abc_freqs)

        # Table of frequences
        self.tvAbcLettersFreqs.setColumnCount(2)
        header = self.tvAbcLettersFreqs.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tvAbcLettersFreqs.setHorizontalHeaderLabels(['Буква', 'Частота'])
        self.tvAbcLettersFreqs.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # Caesar
        self.sbCaesarKey.valueChanged.connect(lambda: self.ciphers['caesar'].set_param('key', self.sbCaesarKey.value()))

        # Affine
        self.sbAffineA.valueChanged.connect(lambda: self.ciphers['affine'].set_param('A', self.sbAffineA.value()))
        self.sbAffineB.valueChanged.connect(lambda: self.ciphers['affine'].set_param('B', self.sbAffineB.value()))
        self.sbAffine_A.valueChanged.connect(lambda: self.ciphers['affine'].set_param('_A', self.sbAffine_A.value()))

        # Viginer
        self.leViginerKey.editingFinished.connect(
            lambda: self.ciphers['viginer'].set_param('key', self.leViginerKey.text()))

        # Gamma
        self.sbGammaA.valueChanged.connect(lambda: self.ciphers['gamma'].set_param('A', self.sbGammaA.value()))
        self.sbGammaB.valueChanged.connect(lambda: self.ciphers['gamma'].set_param('B', self.sbGammaB.value()))
        self.sbGammaM.valueChanged.connect(lambda: self.ciphers['gamma'].set_param('M', self.sbGammaM.value()))
        self.sbGammaInitKey.valueChanged.connect(
            lambda: self.ciphers['gamma'].set_param('key', self.sbGammaInitKey.value()))

        # Feistel
        self.sbFeistelBlockSize.valueChanged.connect(
            lambda: self.ciphers['feistel'].set_param('block_size', self.sbFeistelBlockSize.value()))
        self.sbFeistelRounds.valueChanged.connect(
            lambda: self.ciphers['feistel'].set_param('rounds', self.sbFeistelRounds.value()))
        self.leFeistelEmptyChar.editingFinished.connect(
            lambda: self.ciphers['feistel'].set_param('empty_char', self.leFeistelEmptyChar.text()))
        self.sbFeistelA.valueChanged.connect(lambda: self.ciphers['feistel'].set_param('A', self.sbFeistelA.value()))
        self.sbFeistelB.valueChanged.connect(lambda: self.ciphers['feistel'].set_param('B', self.sbFeistelB.value()))
        self.sbFeistelM.valueChanged.connect(lambda: self.ciphers['feistel'].set_param('M', self.sbFeistelM.value()))
        self.sbFeistelInitKey.valueChanged.connect(
            lambda: self.ciphers['feistel'].set_param('key', self.sbFeistelInitKey.value()))

    def load_toolbox_values(self):
        # Abc values
        self.sbAbcLength.setValue(self.abc.length)
        self.leAbcFL.setText(chr(self.abc.fl))
        self.leAbcFU.setText(chr(self.abc.fu))
        self.dsbAbcFrequency.setValue(self.abc.index_coincidence)
        self.sbFreqKeyFrom.setValue(1)
        self.sbFreqKeyFrom.setMinimum(1)
        self.sbFreqKeyTo.setValue(10)
        self.sbFreqKeyTo.setMaximum(100)

        # Caesar
        self.sbCaesarKey.setValue(self.ciphers['caesar'].key)

        # Affine
        self.sbAffineA.setValue(self.ciphers['affine'].A)
        self.sbAffineB.setValue(self.ciphers['affine'].B)
        self.sbAffine_A.setValue(self.ciphers['affine']._A)

        # Viginer
        self.leViginerKey.setText(self.ciphers['viginer'].key)

        # Gamma
        self.sbGammaA.setValue(self.ciphers['gamma'].A)
        self.sbGammaB.setValue(self.ciphers['gamma'].B)
        self.sbGammaM.setValue(self.ciphers['gamma'].M)
        self.sbGammaInitKey.setValue(self.ciphers['gamma'].init_key)

        # Feistel
        self.sbFeistelBlockSize.setValue(self.ciphers['feistel'].block_size)
        self.leFeistelEmptyChar.setText(self.ciphers['feistel'].empty_char)
        self.sbFeistelRounds.setValue(self.ciphers['feistel'].rounds)
        self.sbFeistelA.setValue(self.ciphers['feistel'].A)
        self.sbFeistelB.setValue(self.ciphers['feistel'].B)
        self.sbFeistelM.setValue(self.ciphers['feistel'].M)
        self.sbFeistelInitKey.setValue(self.ciphers['feistel'].init_key)

    def load_ciphers_to_cmb_cur_cipher(self):
        key_translate_dict = {
            'caesar': "Шифр Цезаря",
            'affine': "Аффинный шифр",
            'viginer': "Шифр Вижнера",
            'gamma': "Гамма шифр",
            'feistel': "Блочное шифрование Фейстеля",
        }
        for key, translate in key_translate_dict.items():
            self.cmbCurCipher.addItem(translate, key)

    def load_abc_freqs(self):
        if len(self.leAbcSourcePath.text().strip()) == 0:
            return
        with open(self.leAbcSourcePath.text(), 'rt', encoding=self.encoding) as f:
            self.abc.text = f.read().strip()
            self.abc.__reload__()
        self.update_abc_freqs()

    def update_abc_freqs(self):
        self.tvAbcLettersFreqs.setRowCount(self.abc.length)
        TabItem = QtWidgets.QTableWidgetItem
        for row_index, (letter, freq) in enumerate(self.abc.frequencies):
            self.tvAbcLettersFreqs.setItem(row_index, 0, TabItem(letter))
            self.tvAbcLettersFreqs.setItem(row_index, 1, TabItem(str(freq)))

    # For set minimal range
    def _freq_key_from_changed_(self):
        val = self.sbFreqKeyFrom.value()
        self.sbFreqKeyTo.setMinimum(val)

    # For set maximal range
    def _freq_key_to_changed_(self):
        val = self.sbFreqKeyTo.value()
        self.sbFreqKeyFrom.setMaximum(val)

    # Start thread with frequency analysis
    def do_freq_analysis(self):
        if self.cur_thread and self.cur_thread.isRunning():
            return
        ciphered_text = self.ptOutText.toPlainText()
        key_from = self.sbFreqKeyFrom.value()
        key_to = self.sbFreqKeyTo.value()

        freq_analysis = FrequencyAnalysis(ciphered_text, self.abc, key_len_from=key_from, key_len_to=key_to)

        self.cur_thread = FrequencyThread(freq_analysis)
        self.cur_thread.state.connect(self.show_thread_state)
        self.cur_thread.output.connect(self.deciphering_by_freq_analysis)
        self.cur_thread.start()
        # Handle user choice of result frequency analysis

    def deciphering_by_freq_analysis(self, key_word):
        caption = f"Частотный анализ показал, что ключом является: '{key_word}'\n"
        cipher_title = 'viginer'  # By default use viginer

        if len(key_word) == 1:  # In case one letter use caesar
            cipher_title = 'caesar'
            key_word = self.abc.to_code(key_word)
            caption += "Расшифровать полученным ключом с помощью шифра Цезаря?"
        else:
            caption += "Расшифровать полученным ключом с помощью шифра Вижнера?"
        user_choice = QtWidgets.QMessageBox.question(
            self,
            "Результат частотного анализа",
            caption,
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.Yes
        )
        if user_choice == QtWidgets.QMessageBox.Yes:
            # Use own viginer/caesar to decipher text by hacked code word
            temp_key = self.ciphers[cipher_title].key  # Save setted key-word
            temp_cipher = self.current_cipher  # Save last-used cipher
            self.ciphers[cipher_title].key = key_word  # Set hacked key-word
            self.set_cipher(cipher_title)  # Set as current cipher

            self.decipher_text()  # turn deciphering

            self.current_cipher = temp_cipher  # Return last used cipher
            self.ciphers[cipher_title].key = temp_key  # Return setted key-word
