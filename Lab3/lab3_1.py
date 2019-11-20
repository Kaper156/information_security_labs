from functools import reduce

from Labs_main.common.misc import *
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


def get_n_rows_of_letters(text: list, n: int):
    # text = get_only_letters(text)
    return grouper(text, n)


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

'''
            
        
'''


def get_coincidence_index(enc_letters: str, gamma: int):
    # Gamma - len of key
    indexes = [0] * gamma
    row_len = len(enc_letters) / gamma
    for each_g in range(gamma):  # If gamma=4: 1,2,3,4
        freqs_abc = [0] * ABC_LENGTH
        for i in range(each_g, len(enc_letters), gamma):
            letter_code = get_let_code(enc_letters[i])
            freqs_abc[letter_code] += 1
        for j in range(ABC_LENGTH):
            indexes[each_g] += freqs_abc[j] * (freqs_abc[j] - 1)
        indexes[each_g] = indexes[each_g] / (row_len * (row_len - 1))
    avg_index = sum(indexes) / gamma
    return avg_index


def offset_abc(letters: list, offset: int):
    k = [chr(offset + ord(letter)) for letter in ABC_FREQ.keys()]
    return dict(zip(k, map(lambda l: letters.count(l) / len(letters), ABC_FREQ.keys())))


def offset_letter(letter: str, offset: int):
    reg_offset = get_first_letter_by_register(letter)
    return chr(reg_offset + (get_let_code(letter) + offset) % ABC_LENGTH)


def hack_caesar_by_freq(enc_letters):
    # Сравнить частоты и частоты заданные (с погрешностью)
    # Получим разницу между буквами в первом и втором словарях
    # Это ключ
    # enc_letters_freq = abc_freq_def_copy()

    enc_freqs = dict(zip(ABC_FREQ.keys(), map(lambda l: enc_letters.count(l) / len(enc_letters), ABC_FREQ.keys())))
    typic_freqs = dict(zip(ABC_FREQ.keys(), ABC_FREQ.values()))

    pogreshnosti = list()
    for offset in range(ABC_LENGTH):
        max_E = 1
        for l, f in enc_freqs.items():
            # real_let = chr(((ord(l) - ord(ABC_UPPER_FIRST) + offset) % ABC_LENGTH) + ord(ABC_UPPER_FIRST))
            offseted_letter_freq = enc_freqs[offset_letter(l, offset)]
            typic_letter_freq = typic_freqs[l]
            diff = abs(offseted_letter_freq - typic_letter_freq)
            max_E = min(diff, max_E)
        pogreshnosti.append((offset, max_E))

    pogreshnosti = sorted(pogreshnosti, key=lambda x: x[1])
    _, Es = zip(pogreshnosti)

    offset = pogreshnosti[0][0]
    return chr(ord(ABC_UPPER_FIRST) + offset)

    # '''
    # Find similar and get avg of diff between letters
    #
    # '''
    # simmilar = dict()
    # for typic_letter, typic_freq in typic_freqs:
    #     simmilar[typic_letter] = ABC_UPPER_FIRST, 1  # cause 1 is max
    #     freq = 0
    #     for enc_let, enc_freq in enc_freqs:
    #         diff = abs(typic_freq - enc_freq)
    #         if diff < simmilar[typic_letter][1]:
    #             simmilar[typic_letter] = enc_let, diff
    #             freq = enc_freq
    #     # delete from enc similar
    #     enc_freqs.remove((simmilar[typic_letter][0], freq))
    #
    # differences = list(map(lambda item: ord(item[0]) - ord(item[1][0]), simmilar.items()))
    #
    # avg = sum(differences) / len(differences)
    # print(avg)
    '''
    Find similar and get avg of diff between letters

    '''
    # enc = dict(enc_freqs)
    # typic = dict(typic_freqs)
    #
    # # similiar = list(zip(ABC_FREQ.keys(), [1] * ABC_LENGTH))
    # differences = list()  # [0] * ABC_LENGTH
    # for t_let, t_freq in typic.items():
    #     sim_letter = ABC_UPPER_FIRST
    #     sim_freq = 1
    #     for e_let, e_freq in enc.items():
    #         diff = abs(t_freq - e_freq)
    #         if diff < sim_freq:
    #             sim_letter = e_let
    #             sim_freq = e_freq
    #     del enc[sim_letter]
    #     differences.append(ord(t_let) - ord(sim_letter))
    #
    # print(differences)
    # avg = round(sum(differences) / len(differences))
    # print(avg)
    # return chr(ord(ABC_UPPER_FIRST) + avg)
    '''
    With sorted dicts comparing
    '''
    # enc_freq = sorted(enc_freq, key=lambda x: x[1])
    # typic_freq = sorted(typic_freq, key=lambda x: x[1])
    # print(enc_freq)
    # print(typic_freq)
    # diff_letters = enc_freq[0][0], typic_freq[0][0]
    # return chr(ord(ABC_LOWER_FIRST) + ord(diff_letters[1]) - ord(diff_letters[0]))

    '''
    Old style
    '''
    # enc_letters_freq = [0] * ABC_LENGTH
    # typic_freq = abc_freq_to_list(ABC_FREQ)
    #
    # for let_code in range(ABC_LENGTH):
    #     enc_letters_freq[let_code] = enc_letters.count(chr(ord(ABC_LOWER_FIRST) + let_code)) / len(enc_letters)
    #
    # offset = -1
    # while offset < ABC_LENGTH:
    #     offset += 1
    #     for let_index in range(ABC_LENGTH):
    #         enc_index = (let_index + offset) % ABC_LENGTH
    #         diff = typic_freq[let_index] - enc_letters_freq[enc_index]
    #         if abs(diff) > ABC_FREQ_E:
    #             break
    #
    # return chr(ord(ABC_LOWER_FIRST) - offset)


def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def split_iter(letters: list, n: int):
    local_copy = letters.copy()
    length = (len(letters) // n) * n
    for i in range(n):
        yield [local_copy[j + i] for j in range(0, length, n)]


def brute(encrypted_text: str):
    coincidence_index = 0
    enc_letters = get_only_letters(encrypted_text.upper())
    key_len = 4  # TODO del
    # while coincidence_index < ABC_INDEX_COINCIDENCE and key_len < 20:
    #     key_len += 1
    #     coincidence_index = get_coincidence_index(enc_letters, key_len)
    #     print(f"Index equal {coincidence_index} at {key_len} key length")
    # rows = chunkIt(enc_letters, key_len)
    key_word = str()
    # for row in rows:
    #     key_word += hack_caesar_by_freq(row)
    #
    row_len = len(enc_letters) // key_len
    rows = split_iter(enc_letters, key_len)
    for row in rows:
        # print(row)
        key_word += hack_caesar_by_freq(row)
    print(key_word)


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
    #
    # text = """
    # AAAA
    # BBBB
    # CCCC
    # DDDD
    # EE
    # """
    code = "CODE" or input("Enter code:")
    text = viginer(text, code)
    print(f"Text encrypted with codeword: {code}")
    # brute_force(text)
    brute(text)
