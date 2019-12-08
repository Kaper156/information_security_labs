from RGR.ciphers.cipher import LetterCipher


class GammaCipher(LetterCipher):
    def letter_cipher(self, let_code, key):
        return self.abc.offset_let_code(let_code, key)

    def letter_decipher(self, let_code, key):
        return self.abc.offset_let_code(let_code, -key)

    def key_gen(self, is_cipher: bool):
        last_key = self.init_key
        while True:
            last_key = (last_key * self.A + self.B) % self.M
            yield last_key

    def set_up_parameters(self, params: dict):
        self.A = params['A']
        self.B = params['B']
        self.M = params['M']
        self.init_key = params['key']
