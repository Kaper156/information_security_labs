import unittest

from RGR.ciphers.caesar import CaesarCipher
from RGR.ciphers.viginer import ViginerCipher
from RGR.core.alphabet import load_english
from RGR.core.frequency import FrequencyAnalysis


class FrequencyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.abc = load_english()
        with open('./source_texts/mobydick.txt', 'rt') as f:
            self.big_text = f.read().strip()

    def test_caesar_hack(self):
        from random import randint
        code = randint(1, self.abc.length - 1)
        cipher = CaesarCipher(self.abc, {
            'key': code
        })
        code = self.abc.to_letter(code, is_upper=True)  # Make char from code
        ciphered_text = cipher.ciphering(self.big_text)
        fa = FrequencyAnalysis(ciphered_text, self.abc, key_len_from=0, key_len_to=8)
        self.assertEqual(code, fa.hack_key_word())

    def test_can_hack_4_length_code(self):
        code = "HEIL"
        cipher = ViginerCipher(self.abc, {
            'key': code
        })
        ciphered_text = cipher.ciphering(self.big_text)
        fa = FrequencyAnalysis(ciphered_text, self.abc, key_len_from=0, key_len_to=8)
        self.assertEqual(code, fa.hack_key_word())

    def test_can_hack_12_length_code(self):
        code = "WARISHELLMAN"
        cipher = ViginerCipher(self.abc, {
            'key': code
        })
        ciphered_text = cipher.ciphering(self.big_text)
        fa = FrequencyAnalysis(ciphered_text, self.abc, key_len_from=0, key_len_to=24)
        self.assertEqual(code, fa.hack_key_word())
