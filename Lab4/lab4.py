from Lab3.lab3_1 import offset_letter


def gamma_key(lastkey: int, a: int, b: int, m: int):
    return (lastkey * a + b) % m


def gamma_cipher(text, key: int, a: int, b: int, m: int):
    for letter in text:
        # yield ord(letter) ^ key
        if not letter.isalpha():
            yield letter
            continue
        yield offset_letter(letter, key)
        key = gamma_key(key, a, b, m)


def gamma_decipher(text, key: int, a: int, b: int, m: int):
    for letter in text:
        if not letter.isalpha():
            yield letter
            continue
        yield offset_letter(letter, -key)
        key = gamma_key(key, a, b, m)


def test():
    text = "Some text"
    a, b, m = 3, 2, 40692
    key = 25
    ciphered = list(gamma_cipher(list(text), key, a, b, m))
    print(ciphered)
    deciphered = "".join(list(gamma_decipher(ciphered, key, a, b, m)))
    print(deciphered)
    # assert deciphered == text


from Labs_main.settings.main import FILE_PATH_INPUT_LARGE

if __name__ == '__main__':

    text = ''
    with open(FILE_PATH_INPUT_LARGE, 'rt', encoding='utf8') as f:
        text = f.read().strip()
    a = 3   # int(input("Please enter A value:")) or
    b = 2   # int(input("Please enter B value:")) or
    m = 40692   # int(input("Please enter M value:")) or
    key = 25   # int(input("Please enter start key:")) or
    print(f"Part of the text before ciphering: \n{text[:200]}")
    print()
    print("CIPHERING")
    print()
    ciphered = "".join(gamma_cipher(text, key, a, b, m))
    print(f"Part of the ciphered text: \n{ciphered[:200]}")

    print()
    print("DECIPHERING")
    print()
    deciphered = "".join(gamma_decipher(ciphered, key, a, b, m))
    print(f"Part of the deciphered text: \n{deciphered[:200]}")
