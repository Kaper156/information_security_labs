ABC_LENGTH = 26
ABC_UPPER_FIRST = 'A'
ABC_LOWER_FIRST = 'a'
FILE_PATH_INPUT = 'text.txt'
FILE_PATH_OUT = 'lab2_1.out.txt'


def register(letter):
    return [ord(ABC_UPPER_FIRST), ord(ABC_LOWER_FIRST)][int(letter.islower())]


def caesar_cipher(letter: str, key: int):
    if not letter.isalpha():
        return letter
    return chr((ord(letter) - register(letter) + key) % ABC_LENGTH + register(letter))


def in_one_string():
    key = int(input("Enter key:"))
    L = ABC_LENGTH
    A = ABC_UPPER_FIRST
    a = ABC_LOWER_FIRST
    return "".join(map(
        lambda x: chr(
            (ord(x) + key - (ord(a) if x.islower() else ord(A))) % L
            + (ord(a) if x.islower() else ord(A))) if x.isalpha() else x,
        open(FILE_PATH_INPUT, 'rt').read()))


if __name__ == '__main__':
    print(in_one_string())
    with open(FILE_PATH_INPUT, 'rt') as f_in:
        text = f_in.read()
    key = int(input("Enter key:"))
    cipher = "".join(map(lambda x: caesar_cipher(x, key), text))
    with open(FILE_PATH_OUT, 'wt') as f:
        f.write(cipher)
    print(cipher)
