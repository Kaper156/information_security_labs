from abc import ABC, abstractmethod

from RGR.core.alphabet import Alphabet


class Cipher(ABC):
    def __init__(self, abc: Alphabet, params: dict):
        self.abc = abc
        self.set_up_parameters(params)

    @abstractmethod
    def set_up_parameters(self, params: dict):
        pass

    @abstractmethod
    def ciphering(self, text):
        return text

    @abstractmethod
    def deciphering(self, ciphered_text):
        return ciphered_text


class LetterCipher(Cipher, ABC):
    # Handle each letter: send letter-code to letter-cipher/decipher with key, chr it back with register
    def letter_handler(self, let, code, func):
        return self.abc.to_letter(
            code=func(
                ord(let) - self.abc.get_abc_offset(let),
                code
            ),
            is_upper=let.isupper()
        )

    # Encodes a letter by code and key
    @abstractmethod
    def letter_cipher(self, let_code, key):
        pass

    # Decodes a letter by code and key
    @abstractmethod
    def letter_decipher(self, let_code, key):
        pass

    # Every letter call next to this generator
    @abstractmethod
    def key_gen(self, is_cipher: bool):
        from itertools import cycle
        return cycle([None])

    # Encodes a whole text
    def ciphering(self, text):
        return self.text_transformation(text=text, is_cipher=True)

    # Decodes a whole text
    def deciphering(self, ciphered_text):
        return self.text_transformation(text=ciphered_text, is_cipher=False)

    # Because encode/decode very similar, here occur operations on text and call code/decode for each letter
    def text_transformation(self, text, is_cipher):
        result = ''
        keys = self.key_gen(is_cipher)
        func = None
        if is_cipher:
            func = self.letter_cipher
        else:
            func = self.letter_decipher
        for letter in text:
            if not self.abc.is_own_letter(letter):
                result += letter
                continue
            code = next(keys)
            result += self.letter_handler(letter, code, func)
        return result
