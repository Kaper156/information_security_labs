from RGR.ciphers.cipher import LetterCipher


class CaesarCipher(LetterCipher):
    def letter_cipher(self, let_code, key):
        return self.abc.offset_let_code(let_code, key)

    def letter_decipher(self, let_code, key):
        # As the key for decipher is multiplied by -1, we can simply use the same function
        return self.letter_cipher(let_code, key)

    def key_gen(self, is_cipher: bool):
        from itertools import cycle
        if is_cipher:
            return cycle([self.key])
        else:
            return cycle([-self.key])

    def set_up_parameters(self, params: dict):
        self.key = int(params['key'])
