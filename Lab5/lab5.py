from Lab4.lab4 import gamma_key_gen

BLOCK_SIZE = 64
EMPTY_CHAR = ' '


def text_to_blocks(text: str, block_size=BLOCK_SIZE, empty_char=EMPTY_CHAR):
    a = len(text) - block_size * (len(text) // block_size)
    if a > 0:  # Check text-length and length of all blocks
        text += empty_char * (block_size - a)  # Add whitespaces for last block which less than block-size
    blocks = [text[i: i + block_size] for i in range(0, len(text), block_size)]
    return blocks


def strip_empty(text: str, empty_char=EMPTY_CHAR):
    while text.endswith(empty_char):
        text = text[:-1]
    return text


def split_block(block: str):
    half = len(block) // 2
    assert (len(block) % 2) == 0  # Only even
    return block[half:], block[:half]


def join_parts(left: str, right: str):
    return left + right


def cipher_f(data, key, unsafe=False):
    res = ''
    for s in data:
        if unsafe:
            res += chr(ord(s) + key)
        else:
            bl = ord(s).bit_length()
            mask = 2 ** (bl + 1) - 1
            res += chr(ord(s) ^ (key & mask))
    return res


def xor_parts(left, right):
    res = ''
    for i in range(len(left)):
        l = ord(left[i])
        r = ord(right[i])
        res += chr(l ^ r)
    return res


def feistel_cipher(text, keys, rounds, block_size=BLOCK_SIZE):
    result = ''
    for block in text_to_blocks(text, block_size):
        left, right = split_block(block)
        for i in range(rounds):
            swap = xor_parts(cipher_f(left, keys[i]), right)
            right = left
            left = swap
        result += join_parts(left, right)
    return result


def feistel_decipher(block, keys, rounds, block_size=BLOCK_SIZE):
    keys = list(reversed(keys))
    result = feistel_cipher(block, keys, rounds, block_size=block_size)
    return strip_empty(result)


def test():
    text = 'Some Short tExt С кириЛецией'
    with open(FILE_PATH_INPUT_LARGE, 'rt', encoding='utf8') as f:
        text = f.read().strip()
    rounds = 6
    b_size = 32
    from Lab4.lab4 import gamma_key_gen

    a = 15
    b = 5312
    m = 40692
    first_key = 25
    keys = list(gamma_key_gen(first_key, a, b, m, rounds))

    ciphered = feistel_cipher(text, keys, rounds, b_size)
    deciphered = feistel_decipher(ciphered, keys, rounds, b_size)
    assert text == deciphered


if __name__ == '__main__':
    from Labs_main.settings.main import FILE_PATH_INPUT_LARGE

    test()
    text = input('Input text or blank to load big text-file')
    if not text.strip():
        with open(FILE_PATH_INPUT_LARGE, 'rt', encoding='utf8') as f:
            text = f.read().strip()
    rounds = int(input('Please enter num of rounds:') or 5)
    b_size = int(input('Please enter block size:') or BLOCK_SIZE)

    print("For ciphering used gamma key. Please enter following parameters.")

    a = int(input("A:") or 26)
    b = int(input("B:") or 41)
    m = int(input("M:") or 4096)

    first_key = int(input("Initial key:") or 215)
    keys = list(gamma_key_gen(first_key, a, b, m, rounds))

    ciphered = feistel_cipher(text, keys, rounds, b_size)
    deciphered = feistel_decipher(ciphered, keys, rounds, b_size)
    print()
    print("\tText before ciphering:")
    if len(text) < 200:
        print(text)
    else:
        print(text[:200])
    print()

    print("\tText after ciphering")
    if len(ciphered) < 200:
        print(ciphered)
    else:
        print(ciphered[:200])
    print()

    print("\tText after deciphering")
    if len(deciphered) < 200:
        print(deciphered)
    else:
        print(deciphered[:200])
