class AlphabetCreationException(Exception):
    pass


class Alphabet:
    def __init__(self, length: int,
                 lower_first_letter: str, upper_first_letter: str,
                 index_coincidence: float, frequencies: tuple = None, text: str = None):

        self.length = length
        self.fl = ord(lower_first_letter)
        self.fu = ord(upper_first_letter)
        if frequencies is None:
            if text is None:
                raise AlphabetCreationException()
            frequencies = self.calc_frequencies(text)

        if len(frequencies) != length:
            raise AlphabetCreationException()

        self.frequencies = frequencies
        self.index_coincidence = index_coincidence

    def calc_frequencies(self, text: str):
        letters = list(map(lambda let_code: chr(let_code), range(self.fl, self.fl + self.length)))

        letters_of_text = "".join(filter(lambda term: term in letters, text.lower()))
        return [(letter, letters_of_text.count(letter) / len(letters_of_text)) for letter in letters]

    def offset_letter(self, letter: str, offset: int):
        abc_off = self.get_abc_offset(letter)
        return chr(abc_off + (ord(letter) - abc_off + offset) % self.length)

    def offset_let_code(self, code: int, offset: int):
        return (code + offset) % self.length

    def get_abc_offset(self, letter: str):
        return [self.fl, self.fu][letter.isupper()]

    def to_code(self, letter: str):
        return ord(letter) - self.get_abc_offset(letter)

    def to_letter(self, code: int, is_upper=False):
        if is_upper:
            return chr(self.fu + (code % self.length))
        return chr(self.fl + (code % self.length))


def load_english() -> Alphabet:
    freqs = (('a', 0.0817), ('b', 0.0149), ('c', 0.0278), ('d', 0.0425), ('e', 0.127), ('f', 0.0223), ('g', 0.0202),
             ('h', 0.060899999999999996), ('i', 0.0697), ('j', 0.0015), ('k', 0.0077), ('l', 0.0403), ('m', 0.0241),
             ('n', 0.0675), ('o', 0.0751), ('p', 0.019299999999999998), ('q', 0.001), ('r', 0.0599), ('s', 0.0633),
             ('t', 0.0906), ('u', 0.0276), ('v', 0.0098), ('w', 0.0236), ('x', 0.0015), ('y', 0.0197), ('z', 0.0005))
    return Alphabet(26, 'a', 'A', 0.06497, freqs)
