import unittest

from RGR.main.alphabet import load_english, Alphabet


class AlphabetOffsetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.abc = load_english()

    def test_offset_a_shifted_to_0(self):
        expected = 'a'
        value = 'a'
        offset = 0
        self.assertEqual(expected, self.abc.offset_letter(value, offset))

    def test_offset_z_shifted_to_0(self):
        expected = 'z'
        value = 'z'
        offset = 0
        self.assertEqual(expected, self.abc.offset_letter(value, offset))

    def test_offset_A_shifted_to_0(self):
        expected = 'A'
        value = 'A'
        offset = 0
        self.assertEqual(expected, self.abc.offset_letter(value, offset))

    def test_offset_A_shifted_to_C(self):
        expected = 'C'
        value = 'A'
        offset = self.abc.to_code('C')
        self.assertEqual(expected, self.abc.offset_letter(value, offset))

    def test_offset_a_shifted_to_abc_length(self):
        expected = 'a'
        value = 'a'
        offset = self.abc.length
        self.assertEqual(expected, self.abc.offset_letter(value, offset))


class AlphabetToCodeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.abc = load_english()

    def test_to_code_a(self):
        expected = 0
        value = 'a'
        self.assertEqual(expected, self.abc.to_code(value))

    def test_to_code_A(self):
        expected = 0
        value = 'A'
        self.assertEqual(expected, self.abc.to_code(value))

    def test_to_code_z(self):
        expected = 25
        value = 'z'
        self.assertEqual(expected, self.abc.to_code(value))

    def test_to_code_Z(self):
        expected = 25
        value = 'Z'
        self.assertEqual(expected, self.abc.to_code(value))


class AlphabetFromCodeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.abc = load_english()

    def test_to_letter_lower_0(self):
        expected = 'a'
        value = 0
        self.assertEqual(expected, self.abc.to_letter(value, is_upper=False))

    def test_to_letter_lower_25(self):
        expected = 'z'
        value = 25
        self.assertEqual(expected, self.abc.to_letter(value, is_upper=False))

    def test_to_letter_lower_51(self):
        expected = 'z'
        value = 51
        self.assertEqual(expected, self.abc.to_letter(value, is_upper=False))

    def test_to_letter_upper_0(self):
        expected = 'A'
        value = 0
        self.assertEqual(expected, self.abc.to_letter(value, is_upper=True))

    def test_to_letter_upper_25(self):
        expected = 'Z'
        value = 25
        self.assertEqual(expected, self.abc.to_letter(value, is_upper=True))

    def test_to_letter_upper_51(self):
        expected = 'Z'
        value = 51
        self.assertEqual(expected, self.abc.to_letter(value, is_upper=True))


class AlphabetCreationWithoutFreqsTests(unittest.TestCase):
    def test_create_from_mobydick(self):
        etallon = load_english()
        with open('./source_texts/mobydick.txt', 'rt') as f:
            big_text = f.read().strip()
        abc = Alphabet(etallon.length,
                       chr(etallon.fl), chr(etallon.fu),
                       etallon.index_coincidence,
                       frequencies=None, text=big_text)
        sum_of_freqs = sum([freq for _, freq in abc.frequencies])
        self.assertAlmostEqual(1.0, sum_of_freqs, 4)
