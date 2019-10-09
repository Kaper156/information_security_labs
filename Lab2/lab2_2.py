from Lab2.lab2_1 import register
from Lab2.lab2_settings import *


def affine_cipher(letter, A, B):
    if not letter.isalpha():
        return letter

    return chr(((ord(letter) - register(letter)) * A + B) % ABC_LENGTH + register(letter))


if __name__ == '__main__':
    with open(FILE_PATH_INPUT, 'rt') as f_in:
        text = f_in.read()
    key_a = int(input("Enter key A:"))
    key_b = int(input("Enter key B:"))
    cipher = "".join(map(lambda x: affine_cipher(x, key_a, key_b), text))
    with open(FILE_PATH_OUT, 'wt') as f:
        f.write(cipher)
    print(cipher)
