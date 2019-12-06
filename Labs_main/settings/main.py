import os

ABC_LENGTH = 26
ABC_UPPER_FIRST = 'A'
ABC_LOWER_FIRST = 'a'
BASE_FOLDER = os.path.normpath(os.path.join(os.getcwd(), os.pardir))
SRC_FOLDER = os.path.normpath(os.path.join(BASE_FOLDER, "Labs_main", "src_text"))
FILE_PATH_INPUT = os.path.normpath(os.path.join(SRC_FOLDER, 'text.txt'))
# FILE_PATH_INPUT_LARGE = os.path.normpath(os.path.join(SRC_FOLDER, 'mobydick.txt'))
FILE_PATH_INPUT_LARGE = os.path.normpath(os.path.join(SRC_FOLDER, 'the last story of old oak.txt'))
