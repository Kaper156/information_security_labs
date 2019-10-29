from Lab2.lab2_settings import ABC_UPPER_FIRST, ABC_LOWER_FIRST


def register(letter):
    return [ord(ABC_UPPER_FIRST), ord(ABC_LOWER_FIRST)][int(letter.islower())]
