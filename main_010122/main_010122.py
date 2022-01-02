################################################
# 1. Создать папку ./alphabet/ Если папка существует, то ОК.
# 2. В папке ./alphabet/ создать файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.

import os
import string
import random

dir_name = 'alphabet'
os.makedirs(dir_name, exist_ok=True)

letters = string.ascii_lowercase

for symbol in letters:
    write_str = letters.replace(symbol, symbol.upper())
    file_name = f"{symbol}.txt"
    file_path = os.path.join(dir_name, file_name)
    with open(file_path, 'w') as txt_file:
        txt_file.write(write_str)

while len(os.listdir(dir_name)) > 13:
    remove_file_name = f"{os.listdir(dir_name)[random.randint(0, len(os.listdir(dir_name)) - 1)]}"
    remove_file_path = os.path.join(dir_name, remove_file_name)
    os.remove(remove_file_path)
