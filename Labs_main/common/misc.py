from Lab2.lab2_settings import ABC_UPPER_FIRST, ABC_LOWER_FIRST, ABC_FREQ


def get_first_letter_by_register(letter):
    return [ord(ABC_UPPER_FIRST), ord(ABC_LOWER_FIRST)][int(letter.islower())]


def get_let_code(letter):
    return ord(letter) - get_first_letter_by_register(letter)

def abc_freq_def_copy():
    from collections import defaultdict
    return defaultdict(lambda: 0, ABC_FREQ)

def abc_freq_to_list(abc_freq):
    return [abc_freq[let] for let in sorted(abc_freq.keys())]

# TODO: coroutine
def get_only_letters(text: str):
    return list(filter(lambda l: l.isalpha(), text))


def get_letter_count(text):
    letters = text
    if type(text) is str:
        text = text.upper()
        letters = get_only_letters(text)
    return dict(zip(letters, list(map(lambda l: text.count(l), text))))


def get_letter_freq(text):
    letters = text
    if type(text) is str:
        text = text.upper()
        letters = get_only_letters(text)
    return {let: (count / len(letters))  for let, count in get_letter_count(text).items()}

    # abc = reduce(lambda l, t: t + l, filter(lambda l: l.isalpha(), text.upper()))
    # return dict(zip(abc, list(map(lambda l: (text.count(l) / len(abc)) * 100, text))))
