################################################
# 1. Создать папку ./alphabet/ Если папка существует, то ОК.
# 2. В папке ./alphabet/ создать файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.

import os
import string
import random


DIR_NAME = 'alphabet'
LETTERS = string.ascii_lowercase


def create_dir(dir_name: str) -> None:
    os.makedirs(dir_name, exist_ok=True)


def create_abc_files(dir_name: str, alphabet: str) -> None:
    for symbol in alphabet:
        file_name = f"{symbol}.txt"
        file_path = os.path.join(dir_name, file_name)
        with open(file_path, 'w') as txt_file:
            txt_file.write(alphabet.replace(symbol, symbol.upper()))


def thanos_snap(dir_name: str) -> None:
    snap_point = len(os.listdir(dir_name))
    while len(os.listdir(dir_name)) > snap_point // 2:
        remove_file_name = f"{os.listdir(dir_name)[random.randint(0, len(os.listdir(dir_name)) - 1)]}"
        remove_file_path = os.path.join(dir_name, remove_file_name)
        os.remove(remove_file_path)


create_dir(DIR_NAME)
create_abc_files(DIR_NAME, LETTERS)
thanos_snap(DIR_NAME)




