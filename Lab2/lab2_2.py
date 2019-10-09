from Lab2.lab2_1 import register
from Lab2.lab2_settings import *


def affine_cipher(letter, A, B, decipher=False):
    if not letter.isalpha():
        return letter

    return chr(((ord(letter) - register(letter)) * A + B*(+1 if not decipher else -1)) % ABC_LENGTH + register(letter))


def in_one_string(text=None, ka=None, kb=None, decipher=False):
    key_a = ka or int(input("Enter key:"))
    key_b = kb or int(input("Enter key:"))
    L = ABC_LENGTH
    A = ABC_UPPER_FIRST
    a = ABC_LOWER_FIRST
    return "".join(map(
        lambda x: chr(
            ((ord(x) - (ord(a) if x.islower() else ord(A))) * key_a
                + key_b*(+1 if not decipher else -1)) % L
            + (ord(a) if x.islower() else ord(A))) if x.isalpha() else x,
        text or open(FILE_PATH_INPUT, 'rt').read()))


def test():
    key_a = 3
    key_a_inv = 9
    key_b = ABC_LENGTH + 4
    text = "Some text from abc"
    # text = "ATTACK AT DAWN"

    # ABC length is not important
    assert in_one_string(text, key_a, key_b) == in_one_string(text, key_a, key_b - ABC_LENGTH)

    # Can be deciphered
    ciphered_text = in_one_string(text, key_a, key_b, False)
    assert in_one_string(ciphered_text, key_a_inv, key_b, True) == text

    # Simple test
    text = "ATTACK AT DAWN"
    crypto = in_one_string(text, key_a_inv, key_b)
    assert crypto == "EJJEKI EJ NESR"


if __name__ == '__main__':
    test()
    with open(FILE_PATH_INPUT, 'rt') as f_in:
        text = f_in.read()
    key_a = int(input("Enter key A:"))
    key_b = int(input("Enter key B:"))
    cipher = "".join(map(lambda x: affine_cipher(x, key_a, key_b), text))
    with open(FILE_PATH_OUT, 'wt') as f:
        f.write(cipher)
    print(cipher)
