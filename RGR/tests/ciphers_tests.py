import unittest

from RGR.ciphers.affine import AffineCipher
from RGR.ciphers.caesar import CaesarCipher
from RGR.ciphers.feistel import FeistelCipher
from RGR.ciphers.gamma import GammaCipher
from RGR.ciphers.viginer import ViginerCipher
from RGR.core.alphabet import load_english


class LetterCipherTest(unittest.TestCase):
    def setUp(self) -> None:
        from random import randint
        self.abc = load_english()  # Precompiled english alphabet
        self.ciphers = {
            "Caesar-cipher": CaesarCipher(self.abc, {
                'key': randint(1, self.abc.length)
            }),
            "Affine-cipher": AffineCipher(self.abc, {
                'A': 3,
                'B': 4,
                '-A': 9
            }),
            "Viginer-cipher": ViginerCipher(self.abc, {
                'key': 'coDeWord'
            }),
            "Gamma-cipher": GammaCipher(self.abc, {
                'A': randint(1000, 4000),
                'B': randint(250, 1000),
                'M': 4096,
                'key': randint(1, 4096)
            }),

            "Feistel-block-cipher": FeistelCipher(self.abc, {
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

    def test_text_not_changed_in_process(self):
        text = 'Some small text 12345 WiTh dumB ReGisTeR'
        for cipher_title, cipher in self.ciphers.items():
            text_ciphered = cipher.ciphering(text)
            text_deciphered = cipher.deciphering(text_ciphered)
            self.assertNotEqual(text, text_ciphered, 'Text not ciphered!')
            self.assertEqual(text, text_deciphered, 'Source and decoded text not equal!')
            print(f"{cipher_title} passed")
