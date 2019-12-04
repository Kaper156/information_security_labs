from collections import OrderedDict

from Labs_main.common.misc import *
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


def get_coincidence_index(enc_letters: str, gamma: int):
    # Gamma - expected length of key
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


def offset_letter(letter: str, offset: int):
    reg_offset = get_first_letter_by_register(letter)
    return chr(reg_offset + (get_let_code(letter) + offset) % ABC_LENGTH)


def to_letter(code: int):
    return chr(code + ord(ABC_UPPER_FIRST))


def offset_abc(abc: OrderedDict, offset):
    freqs = iter(list(abc.values()))
    result = OrderedDict()
    for off_letter in (list(abc.keys())[offset:] + list(abc.keys())[:offset]):
        result[off_letter] = next(freqs)
    return OrderedDict(sorted(result.items(), key=lambda item: item[0]))


def hack_caesar_by_freq(enc_letters):
    etallon = OrderedDict(sorted(ABC_FREQ.items(), key=lambda item: item[0]))
    variants = dict()
    enc_abc = OrderedDict({letter: enc_letters.count(letter) / len(enc_letters) for letter in sorted(ABC_FREQ.keys())})

    for offset in range(ABC_LENGTH):
        offseted_abc = offset_abc(enc_abc, offset)
        delta = sum(map(lambda et, enc: abs(et - enc), etallon.values(), offseted_abc.values())) / ABC_LENGTH
        variants[offset] = delta
    code = ABC_LENGTH - min(variants.items(), key=lambda item: item[1])[0]

    return to_letter(code)


def split_iter(letters: list, n: int):
    local_copy = letters.copy()
    length = (len(letters) // n) * n
    for i in range(n):
        yield [local_copy[j + i] for j in range(0, length, n)]


def brute(encrypted_text: str):
    coincidence_index = 0
    enc_letters = get_only_letters(encrypted_text.upper())
    key_len = 0
    while coincidence_index < ABC_INDEX_COINCIDENCE and key_len < 20:
        key_len += 1
        coincidence_index = get_coincidence_index(enc_letters, key_len)
        print(f"Index equal {coincidence_index} at {key_len} key length")
    key_word = str()
    rows = split_iter(enc_letters, key_len)
    for row in rows:
        key_word += hack_caesar_by_freq(row)
    return key_word


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
    print("Part from source text:")
    print(text[:200])
    print()
    code = "CODEWORD" or input("Enter code:")
    text = viginer(text, code)

    print(f"Text encrypted with codeword: {code}")
    print("Part from ciphered text:")
    print(text[:200])
    print()

    key = brute(text)
    assert code.upper() == key  # Test without register checking
    text = viginer(text, key, True)
    print(f"I think codeword is - '{key}'")
    print("Part from deciphered text:")
    print(text[:200])
