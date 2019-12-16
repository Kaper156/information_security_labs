from PyQt5.QtCore import QThread, pyqtSignal

from ciphers.cipher import Cipher


class CipherThread(QThread):
    output = pyqtSignal(str)
    state = pyqtSignal(str)

    def __init__(self, cipher: Cipher, text: str, is_cipher=False):
        QThread.__init__(self)
        self.cipher = cipher
        self.text = text
        self.is_cipher = is_cipher

    def __del__(self):
        self.wait()

    def run(self):
        result = ''
        if self.is_cipher:
            self.state.emit("Начато шифрование")
            result = self.cipher.ciphering(self.text)
            self.state.emit("Шифрование закончено")
        else:
            self.state.emit("Начато дешифрование")
            result = self.cipher.deciphering(self.text)
            self.state.emit("Дешифрование закончено")
        self.output.emit(result)
