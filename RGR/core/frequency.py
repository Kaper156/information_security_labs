from RGR.core.alphabet import Alphabet
from RGR.core.misc import split_iter


class FrequencyAnalysis:
    def __init__(self, text: str, abc: Alphabet, key_len_from=0, key_len_to=20):
        self.text = text
        self.abc = abc
        self.klf = key_len_from
        self.klt = key_len_to

    # Find closest or correct codeword
    # Codeword in UPPER CASE (because letters of codeword used only as shift parameters)
    def hack_key_word(self):
        coincidence_index = 0
        enc_letters = self._get_only_letters_()
        key_len = self.klf
        while coincidence_index < self.abc.index_coincidence and key_len < self.klt:
            key_len += 1
            coincidence_index = self.get_coincidence_index(enc_letters, key_len)
            # print(f"Index equal {coincidence_index} at {key_len} key length")
        key_word = str()
        rows = split_iter(enc_letters, key_len)
        for row in rows:
            key_word += self.find_offset(row)
        return key_word

    # Get only letters from encrypted text (in lower case)
    def _get_only_letters_(self):
        return [let.lower() for let in self.text if let.isalpha()]

    def get_coincidence_index(self, enc_letters: str or tuple, gamma: int):
        # Gamma - expected length of key
        indexes = [0] * gamma
        row_len = len(enc_letters) / gamma
        for each_g in range(gamma):  # If gamma=4: 1,2,3,4
            freqs_abc = [0] * self.abc.length
            for i in range(each_g, len(enc_letters), gamma):
                letter_code = self.abc.to_code(enc_letters[i])
                freqs_abc[letter_code] += 1
            for j in range(self.abc.length):
                indexes[each_g] += freqs_abc[j] * (freqs_abc[j] - 1)
            indexes[each_g] = indexes[each_g] / (row_len * (row_len - 1))
        avg_index = sum(indexes) / gamma
        return avg_index

    def _shift_abc_(self, abc: tuple, shift):
        return sorted([(self.abc.offset_letter(let, -shift), index) for let, index in abc])

    def find_offset(self, enc_letters):
        etallon = self.abc.frequencies
        variants = list()
        encoded = tuple((letter, enc_letters.count(letter) / len(enc_letters)) for letter, _ in etallon)

        for offset in range(self.abc.length):
            shifted = self._shift_abc_(encoded, offset)
            delta = sum(map(lambda et, enc: abs(et[1] - enc[1]), etallon, shifted)) / self.abc.length
            variants.append((offset, delta))

        code = min(variants, key=lambda item: item[1])[0]
        return self.abc.to_letter(code, is_upper=True)
