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
        self.text = text
        self.abc = None
        self.__calc_letters__()

        self.frequencies = frequencies
        self.index_coincidence = index_coincidence

    def __reload__(self):
        self.__calc_letters__()
        if self.text:
            self.frequencies = self.calc_frequencies(self.text)
        else:
            self.__freqs_default__()
        # print(f"{self.fu}\t{self.fl}\t{self.abc}\t{self.length}")

    def __calc_letters__(self):
        self.abc = tuple(map(chr, chain(range(self.fu, self.fu + self.length), range(self.fl, self.fl + self.length))))

    def __freqs_default__(self):
        def_freq = 1 / self.length
        self.frequencies = [(let, def_freq) for let in self.abc]

    def calc_frequencies(self, text: str):
        self.__calc_letters__()  # Reload letters
        letters_of_text = "".join(filter(lambda term: self.is_own_letter(term), text))
        if len(letters_of_text) == 0:  # In case invalid text or abc return old freqs
            return self.frequencies
        return [(letter, letters_of_text.count(letter) / len(letters_of_text)) for letter in self.abc]

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


def load_russian() -> Alphabet:
    freqs = (
        ('о', 10.97 / 100), ('е', 8.45 / 100), ('а', 8.01 / 100), ('и', 7.35 / 100), ('н', 6.70 / 100),
        ('т', 6.26 / 100), ('с', 5.47 / 100), ('р', 4.73 / 100), ('в', 4.54 / 100), ('л', 4.40 / 100),
        ('к', 3.49 / 100), ('м', 3.21 / 100), ('д', 2.98 / 100), ('п', 2.81 / 100), ('у', 2.62 / 100),
        ('я', 2.01 / 100), ('ы', 1.90 / 100), ('ь', 1.74 / 100),
        ('г', 1.70 / 100), ('з', 1.65 / 100), ('б', 1.59 / 100), ('ч', 1.44 / 100), ('й', 1.21 / 100),
        ('х', 0.97 / 100), ('ж', 0.94 / 100), ('ш', 0.73 / 100), ('ю', 0.64 / 100), ('ц', 0.48 / 100),
        ('щ', 0.36 / 100), ('э', 0.32 / 100), ('ф', 0.26 / 100), ('ъ', 0.04 / 100), ('ё', 0.04 / 100),
    )
    return Alphabet(33, 'а', 'А', 0.0553, frequencies=freqs)

def load_english() -> Alphabet:
    freqs = (('a', 0.0817), ('b', 0.0149), ('c', 0.0278), ('d', 0.0425), ('e', 0.127), ('f', 0.0223), ('g', 0.0202),
             ('h', 0.060899999999999996), ('i', 0.0697), ('j', 0.0015), ('k', 0.0077), ('l', 0.0403), ('m', 0.0241),
             ('n', 0.0675), ('o', 0.0751), ('p', 0.019299999999999998), ('q', 0.001), ('r', 0.0599), ('s', 0.0633),
             ('t', 0.0906), ('u', 0.0276), ('v', 0.0098), ('w', 0.0236), ('x', 0.0015), ('y', 0.0197), ('z', 0.0005))
    return Alphabet(26, 'a', 'A', 0.06497, freqs)
