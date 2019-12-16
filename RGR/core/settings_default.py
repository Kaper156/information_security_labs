import os

while "RGR" in os.path.abspath(os.curdir):  # For tests
    os.chdir('..')  # Switch to parent
SOURCE_TEXTS_PATH = os.path.abspath('./source_texts')


def get_texts_paths():
    return [os.path.abspath(os.path.join(SOURCE_TEXTS_PATH, f))
            for f in os.listdir(SOURCE_TEXTS_PATH)
            if os.path.isfile(os.path.join(SOURCE_TEXTS_PATH, f))]


def get_random_text():
    from random import choice
    return choice(get_texts_paths())
