from PyQt5.QtCore import QThread, pyqtSignal

from core.frequency import FrequencyAnalysis


class FrequencyThread(QThread):
    output = pyqtSignal(str)
    state = pyqtSignal(str)

    def __init__(self, frequency: FrequencyAnalysis):
        QThread.__init__(self)
        self.frequency = frequency

    def __del__(self):
        self.wait()

    def run(self):
        self.state.emit("Начат частотный анализ")
        code_word = self.frequency.hack_key_word()
        self.state.emit("Частотный анализ закончен")
        self.output.emit(code_word)
