from itertools import chain


class Alphabet:
    def __init__(self, length: int,
                 lower_first_letter: str, upper_first_letter: str,
                 index_coincidence: float, frequencies: tuple = None, text: str = None):

        self.length = length
        self.fl = ord(lower_first_letter)
        self.fu = ord(upper_first_letter)
        if frequencies is None:
            if text is None:
                self.__freqs_default__()
            else:
                frequencies = self.calc_frequencies(text)

        self.abc = None
        self.__calc_letters__()

        self.frequencies = frequencies
        self.index_coincidence = index_coincidence

    def __reload__(self):
        self.__calc_letters__()
        self.__freqs_default__()
        # print(f"{self.fu}\t{self.fl}\t{self.abc}\t{self.length}")

    def __calc_letters__(self):
        self.abc = tuple(map(chr, chain(range(self.fu, self.fu + self.length), range(self.fl, self.fl + self.length))))

    def __freqs_default__(self):
        def_freq = 1 / self.length
        self.frequencies = [(let, def_freq) for let in self.abc]

    def calc_frequencies(self, text: str):
        letters = list(map(chr, range(self.fl, self.fl + self.length)))

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

    def is_own_letter(self, letter: str):
        return letter in self.abc

    def set_length(self, val: int):
        self.length = val
        self.__reload__()

    def set_fu(self, val: str):
        if len(val):
            self.fu = ord(val[0])
            self.__reload__()

    def set_fl(self, val: str):
        if len(val):
            self.fl = ord(val[0])
            self.__reload__()

    def set_index_coincidence(self, val):
        self.index_coincidence = val


def load_english() -> Alphabet:
    freqs = (('a', 0.0817), ('b', 0.0149), ('c', 0.0278), ('d', 0.0425), ('e', 0.127), ('f', 0.0223), ('g', 0.0202),
             ('h', 0.060899999999999996), ('i', 0.0697), ('j', 0.0015), ('k', 0.0077), ('l', 0.0403), ('m', 0.0241),
             ('n', 0.0675), ('o', 0.0751), ('p', 0.019299999999999998), ('q', 0.001), ('r', 0.0599), ('s', 0.0633),
             ('t', 0.0906), ('u', 0.0276), ('v', 0.0098), ('w', 0.0236), ('x', 0.0015), ('y', 0.0197), ('z', 0.0005))
    return Alphabet(26, 'a', 'A', 0.06497, freqs)
