from Lab2.lab2_settings import ABC_UPPER_FIRST, ABC_LOWER_FIRST, ABC_FREQ


def get_first_letter_by_register(letter):
    return [ord(ABC_UPPER_FIRST), ord(ABC_LOWER_FIRST)][int(letter.islower())]


def abc_freq_def_copy():
    from collections import defaultdict

    return defaultdict(lambda: 0, ABC_FREQ)


# TODO: coroutine
def get_only_letters(text: str):
    return list(filter(lambda l: l.isalpha(), text))


def get_letter_count(text: str):
    text = text.upper()
    letters = get_only_letters(text)
    return dict(zip(letters, list(map(lambda l: text.count(l), text))))


def get_letter_freq(text: str):
    text = text.upper()
    letters = get_only_letters(text)
    return {let: (count / len(letters)) * 100 for let, count in get_letter_count(text).items()}

    # abc = reduce(lambda l, t: t + l, filter(lambda l: l.isalpha(), text.upper()))
    # return dict(zip(abc, list(map(lambda l: (text.count(l) / len(abc)) * 100, text))))
