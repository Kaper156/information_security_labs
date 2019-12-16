import unittest

from RGR.ciphers.caesar import CaesarCipher
from RGR.ciphers.viginer import ViginerCipher
from RGR.core.alphabet import load_english
from RGR.core.frequency import FrequencyAnalysis
from RGR.core.settings_default import get_random_text


class FrequencyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.abc = load_english()
        with open(get_random_text(), 'rt') as f:
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
        hacked_word = fa.hack_key_word()
        deciphered_text = cipher.deciphering(ciphered_text)
        self.assertEqual(code, hacked_word)
        self.assertEqual(self.big_text, deciphered_text)

    def test_can_hack_4_length_code(self):
        code = "HEIL".upper()
        cipher = ViginerCipher(self.abc, {
            'key': code
        })
        ciphered_text = cipher.ciphering(self.big_text)
        fa = FrequencyAnalysis(ciphered_text, self.abc, key_len_from=0, key_len_to=8)
        hacked_word = fa.hack_key_word()
        deciphered_text = cipher.deciphering(ciphered_text)
        self.assertEqual(code, hacked_word)
        self.assertEqual(self.big_text, deciphered_text)

    def test_can_hack_12_length_code(self):
        code = "WARISHELLMAN".upper()
        cipher = ViginerCipher(self.abc, {
            'key': code
        })
        ciphered_text = cipher.ciphering(self.big_text)
        fa = FrequencyAnalysis(ciphered_text, self.abc, key_len_from=0, key_len_to=24)
        hacked_word = fa.hack_key_word()
        print(hacked_word)
        self.assertEqual(code, hacked_word)
        self.assertEqual(self.big_text, deciphered_text)
