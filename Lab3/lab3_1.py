from functools import reduce

from Lab2.lab2_main import *
# from Lab3.lab3_settings import *
from Labs_main.settings.lab3 import *


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


def get_each_n_letter_from_letters(letters, n):
    return [letters[i] for i in range(0, len(letters), n)]


def get_letter_freq_from_letters(letters: list, letter):
    return letters.count(letter) / len(letters)


def brute_force(ciphered_text):
    """
    1. Взять длину (cnt)
    2. Взять из текста только каждый cnt'ый символ/букву
    3. Подсчитать ci
    4. Если полученное ci удовлетворяет = 0.605 то выйти, иначе 5
    5. cnt++, вернутся к 2

    :param ciphered_text:
    :return: source_text
    """
    letters = ciphered_text
    letters = get_only_letters(letters)
    ci = 0
    code_len = 0
    while ci < ABC_INDEX_COINCIDENCE:
        code_len += 1
        n_letters = get_each_n_letter_from_letters(letters, code_len)
        letter_freq = get_letter_freq(n_letters)
        let_len = len(letters)
        C = [0] * code_len
        for i in range(code_len):
            C[i] = reduce(lambda p, lc: p + pow(lc / let_len, 2), letter_freq.values())

        # ci = reduce(lambda p, lc: p + pow(lc/let_len, 2), letter_freq.values())
        ci = max(C)
        print(n_letters)
        print(letter_freq)
        print(ci)
        # for each_i in range(code_len):
        #     ci = reduce(lambda p, lc: p + pow(lc, 2), letters_freq.values())
        # ci = reduce(lambda p, lc: p + pow(lc, 2), letters_freq.values())
        # print(ci)


# https://ru.wikipedia.org/wiki/Индекс_совпадений

def grouper(iterable, n, fillvalue=None):
    from itertools import zip_longest
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def get_n_rows_of_letters(text: str, n: int):
    # text = get_only_letters(text)
    return list(grouper(text, n))


def get_freq_of_each_n_letter(text: str, letter: str, n: int, n_of: int):
    text = get_only_letters(text)
    letter = letter.upper()

    return len(tuple(filter(lambda n_let: n_let[n] == letter, get_n_rows_of_letters(text, n_of)))) / len(text)


def get_each_n_letter_freq(text: str, step: int):
    letters = get_only_letters(text)
    rows = get_n_rows_of_letters(letters, step)

    C = [0] * step

    # for i in range(0, len(letters), step):
    #     for j in range(step):
    #         C[j] += get_freq_of_each_n_letter()len(letters)
    # abc = reduce(lambda l, t: t + l, filter(lambda l: l.isalpha(), letters.upper()))
    # return dict(zip(abc, list(map(lambda l: (letters.count(l) / len(abc)) * 100, letters))))


"""
Имеется зашифрованный текст шифром вижнера.
Требуется подобрать длину ключа, а затем взломать его, как шифр цезаря
Подбор длины:
НЕВЕРНО И ЗАТРАТНО:
1. Взять длину (cnt)
    2. Поделить текст на cnt столбцов
    3. Взять частоты букв в каждом столбце
    4. Если полученное ci удовлетворяет = 0.605 то выйти, иначе 5
5. cnt++, вернутся к 2

ДЕШЕВЛЕ:
1. Взять длину (cnt)
    2. Взять из текста только каждый cnt'ый символ/букву
    3. Подсчитать ci
    4. Если полученное ci удовлетворяет = 0.605 то выйти, иначе 5
5. cnt++, вернутся к 2
"""


def test():
    text = "Some text"
    code = "code"
    cipher = viginer(text, code)
    deciphered = viginer(cipher, code, True)
    assert deciphered == text


if __name__ == '__main__':
    test()
    text = str()
    with open(FILE_PATH_INPUT_LARGE, 'rt') as f:
        text = f.read().strip()
    text = viginer(text, "CODE")
    print("Text encrypted with codeword: CODE")
    brute_force(text)
