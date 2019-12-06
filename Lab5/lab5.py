BIT_LENGTH = 8
BIT_MASK = 2 ** BIT_LENGTH - 1
BIT_OFFSET = BIT_LENGTH // 2 - 1
A = 12
B = 25
M = 40


def gamma(data: int, key: int, gamma_mask: int):
    key = gamma_key(key, A, B, M)
    return key, data ^ ((key * 0xabcd1234) & gamma_mask)


def gamma_key(lastkey: int, a: int, b: int, m: int):
    return (lastkey * a + b) % m


def feistel_cipher(text: str, key: int, rounds: int):
    for letter in map(ord, text):
        mask = 2 ** (letter.bit_length() // 2) - 1
        offset = letter.bit_length() - letter.bit_length() // 2
        left = letter & mask
        right = (letter >> offset) & mask
        gamma_mask = mask >> (letter.bit_length() - mask.bit_length())
        print(f"L={left:b} R={right:b} ({chr(letter)} = {letter:b})")
        for i in range(rounds):
            key, cipher = gamma(right, key, gamma_mask)
            swap = left ^ cipher
            print(f"{i}\tL={left:b} R={right:b} SWAP={swap:b}")
            left = right
            right = swap
            print(f"{i}\tL={left:b} R={right:b} SWAP={swap:b}")
        print(f"L={left:b} R={right:b}")
        yield chr(left | (right << offset))


def feistel_decipher(text: str, key: int, rounds: int):
    for letter in map(ord, text):

        mask = 2 ** (letter.bit_length() // 2) - 1
        offset = letter.bit_length() - letter.bit_length() // 2

        gamma_mask = mask >> (letter.bit_length() - mask.bit_length())
        left = letter & mask
        right = (letter >> offset) & mask
        print(f"L={left:b} R={right:b} ({chr(letter)} = {letter:b})")
        for i in range(rounds):
            key, cipher = gamma(left, key, gamma_mask)
            swap = right ^ cipher
            print(f"{i}\tL={left:b} R={right:b} SWAP={swap:b}")
            right = left
            left = swap
            print(f"{i}\tL={left:b} R={right:b} SWAP={swap:b}")
        print(f"L={left:b} R={right:b}")
        yield chr(left | (right << offset))


if __name__ == '__main__':
    text = "Th"
    # text = "This is SOME text 1230 +3"
    # text = "AB"

    # key = randint(BIT_OFFSET, 2 ** (BIT_LENGTH) - 1)
    key = 8
    rounds = 6
    print('\t\tCIPHERING')
    out = feistel_cipher(text, key, rounds)
    out = "".join(out)
    print(out)
    for i in range(len(text)):
        print(f"{text[i]}\t{bin(ord(text[i]))}\t{out[i]}\t{bin(ord(out[i]))}")

    print('\t\tDECIPHERING')
    results = feistel_decipher(out, key, rounds)
    results = "".join(results)
    print(results)
    for i in range(len(text)):
        print(f"{text[i]}\t{bin(ord(text[i]))}\t{results[i]}\t{bin(ord(results[i]))}")
    # assert results == text
