from RGR.ciphers.cipher import LetterCipher


class AffineCipher(LetterCipher):
    def letter_cipher(self, let_code, key):
        return (self.A * let_code + self.B) % self.abc.length

    def letter_decipher(self, let_code, key):
        return (self._A * (let_code - self.B)) % self.abc.length

    def key_gen(self, is_cipher: bool):
        return super(AffineCipher, self).key_gen(is_cipher=is_cipher)

    def set_up_parameters(self, params: dict):
        self.A = int(params['A'])
        self.B = int(params['B'])
        self._A = int(params['-A'])
