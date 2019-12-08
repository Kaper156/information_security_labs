from RGR.ciphers.cipher import LetterCipher


class ViginerCipher(LetterCipher):

    def letter_cipher(self, let_code, key):
        return (let_code + key) % self.abc.length

    def letter_decipher(self, let_code, key):
        return (let_code - key + self.abc.length) % self.abc.length

    def key_gen(self, is_cipher: bool):
        from itertools import cycle
        return cycle(map(lambda c: ord(c) - self.abc.get_abc_offset(c), self.key))

    def set_up_parameters(self, params: dict):
        self.key = str(params['key'])
