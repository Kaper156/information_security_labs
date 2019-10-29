from Lab2.lab2_main import get_first_letter_by_register, get_only_letters
from Lab2.lab2_main import get_letter_freq
from Lab2.lab2_settings import *


def affine(text, A, B, is_decipher=False):
    result = str()
    if not is_decipher:
        transformation = lambda code: (A * code + B) % ABC_LENGTH
    else:
        transformation = lambda code: (A * (code - B)) % ABC_LENGTH
    for letter in text:
        if not letter.isalpha():
            result += letter
            continue

        offset = get_first_letter_by_register(letter)
        code = ord(letter) - offset
        result += chr(transformation(code) + offset)
    return result


def brute_force(source_text, ciphered_text):
    freq = get_letter_freq(ciphered_text)
    print(freq)
    bruted_text = ciphered_text
    code_len = 1
    index = 0
    get_only_letters(ciphered_text)

    while index != ABC_INDEX_COINCIDENCE:

        index =

        code_len += 1


def test():
    key_a = 3
    key_a_inv = 9
    key_b = 4
    text = "ATTACK AT DAWN"

    # ABC length is not important
    assert affine(text, key_a, key_b) == affine(text, key_a, key_b - ABC_LENGTH)

    # Can be deciphered
    ciphered_text = affine(text, key_a, key_b, False)
    assert affine(ciphered_text, key_a_inv, key_b, True) == text

    # Simple test
    text = "ATTACK AT DAWN"
    ciphered_text = affine(text, key_a, key_b)
    assert ciphered_text == "EJJEKI EJ NESR"

    # Big file with lorem
    # Cipher:
    with open(FILE_PATH_INPUT, 'rt') as f_in:
        text = f_in.read()

    ciphered_text = affine(text, key_a, key_b)
    # Text is ciphered
    assert text != ciphered_text

    # All text is deciphered
    assert affine(ciphered_text, key_a_inv, key_b, True) == text


if __name__ == '__main__':
    test()
    with open(FILE_PATH_INPUT, 'rt') as f_in:
        text = f_in.read()
    key_a = 3 or int(input("Enter key A:"))
    key_b = 2 or int(input("Enter key B:"))
    cipher = "".join(map(lambda x: affine(x, key_a, key_b), text))
    with open(FILE_PATH_OUT, 'wt') as f:
        f.write(cipher)
    print(cipher)
    get_letter_freq(cipher)
    brute_force(text, cipher)
