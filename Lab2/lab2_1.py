from Lab2.lab2_main import register
from Lab2.lab2_settings import *


def caesar_cipher(letter: str, key: int):
    if not letter.isalpha():
        return letter
    return chr((ord(letter) - register(letter) + key) % ABC_LENGTH + register(letter))


def in_one_string(text=None, k=None):
    key = k or int(input("Enter key:"))
    L = ABC_LENGTH
    A = ABC_UPPER_FIRST
    a = ABC_LOWER_FIRST
    return "".join(map(
        lambda x: chr(
            (ord(x) + key - (ord(a) if x.islower() else ord(A))) % L
            + (ord(a) if x.islower() else ord(A))) if x.isalpha() else x,
        text or open(FILE_PATH_INPUT, 'rt').read()))


def brute_force(source_text, ciphered_text):
    key = 0
    bruted_text = ciphered_text
    while source_text != bruted_text:
        bruted_text = in_one_string(ciphered_text, key)
        key += 1
        if key > ABC_LENGTH:
            print("Bad try. It's too difficult for me!")
            break
    print(f'Text bruteforced by key {key}, source text:\n\n{source_text} \n\t And bruteforced text:\n\n{bruted_text} ')


def test():
    key = ABC_LENGTH + 5
    text = "Some text from abc"

    # ABC length is not important
    assert in_one_string(text, key) == in_one_string(text, key - ABC_LENGTH)

    # Can be deciphered
    ciphered_text = in_one_string(text, key)
    assert in_one_string(ciphered_text, -key) == text

    # Simple test
    text = "ABC"
    key = 3
    crypto = in_one_string(text, key)
    assert crypto == "DEF"


if __name__ == '__main__':
    test()
    with open(FILE_PATH_INPUT, 'rt') as f_in:
        text = f_in.read()
    key = int(input("Enter key:"))
    cipher = "".join(map(lambda x: caesar_cipher(x, key), text))
    with open(FILE_PATH_OUT, 'wt') as f:
        f.write(cipher)
    print(f'Encoded by caesar-cipher text:\n\n{cipher}\n\n')
    brute_force(text, cipher)
