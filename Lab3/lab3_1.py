from Lab3.lab3_settings import *
from Lab2.lab2_main import get_first_letter_by_register


def viginer_cipher(l, c):
    return (l + c) % ABC_LENGTH


def viginer_decipher(l, c):
    return (l - c + ABC_LENGTH) % ABC_LENGTH


def viginer(text, code_word, decipher=False):
    from itertools import cycle
    codes = cycle(map(lambda c: ord(c) - get_first_letter_by_register(c), code_word))
    result = str()

    # select (de) cipher function
    if not decipher:
        transformation = viginer_cipher
    else:
        transformation = viginer_decipher

    for letter in text:
        if letter.isalpha():
            code = next(codes)
            abc_off = get_first_letter_by_register(letter)
            let_code = ord(letter) - abc_off
            let_code = transformation(let_code, code)
            result += chr(let_code + abc_off)
        else:
            result += letter
    return result


def test():
    text = "Some text"
    code = "code"
    cipher = viginer(text, code)
    deciphered = viginer(cipher, code, True)
    assert deciphered == text


if __name__ == '__main__':
    test()
