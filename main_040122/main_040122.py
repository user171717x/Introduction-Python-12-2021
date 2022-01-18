import csv
import json
import random
import string

# ALL CONSTANTS NEED TO BE AT START OF FILE OR CONFIG FILE, NO MAGIC NUMBERS AT CODE!!!!!

"""
Функция 1. Создает данные для записи в файл txt.
Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы.
"""

MIN_STR_LEN = 100
MAX_STR_LEN = 1000


def get_rand_str(min_str_len: int, max_str_len: int, letters: str) -> str:
    str_len = random.randint(min_str_len, max_str_len)
    res_string = "".join(random.choice(letters) for _ in range(str_len))
    return res_string


def get_rand_txt_str(min_str_len: int = MIN_STR_LEN, max_str_len: int = MAX_STR_LEN) -> str:
    letters = f"{string.ascii_letters}{string.digits}{string.whitespace[0]}"
    res_text = get_rand_str(min_str_len, max_str_len, letters)
    return res_text


"""
Функция 2. Создает данные для записи в файл json.
Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
(можно с повторениями символов).
Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
такая же, как и вероятность того, что будет типа float или типа bool.
"""

MIN_DICT_LEN = 5
MAX_DICT_LEN = 20


def get_rand_key_value():
    res_int = random.randint(-100, 100)
    res_float = random.random()
    res_bool = random.choice([True, False])
    return random.choice([res_int, res_float, res_bool])


def get_rand_json_dict(min_dict_len: int = MIN_DICT_LEN, max_dict_len: int = MAX_DICT_LEN) -> dict:
    dict_len = random.randint(min_dict_len, max_dict_len)
    res_dict = {f"{get_rand_str(5, 5, string.ascii_lowercase)}": get_rand_key_value() for _ in range(dict_len)}
    return res_dict


"""
Функция 3. Создает данные для записи в файл csv.
Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
Числа n и m выбираются случайно в диапазоне от 3 до 10.
В таблицу записывать значения только 0 или 1.
Заголовка у таблицы нет.
"""

MIN_T_LIMIT = 3
MAX_T_LIMIT = 10


def get_rand_csv_table() -> list:
    n_rows = random.randint(MIN_T_LIMIT, MAX_T_LIMIT)
    m_cells = random.randint(MIN_T_LIMIT, MAX_T_LIMIT)
    table = [[random.randint(0, 1) for _ in range(m_cells)] for _ in range(n_rows)]
    return table


"""
Функция 4. Написать функцию generate_and_write_file которая принимает один параметр - полный путь к файлу.
В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
"""

TXT_FILE_PATH = '/home/user/Загрузки/Phyton/Pycharm_projects/Introduction-Python-12-2021/main_040122/test.txt'
JSON_FILE_PATH = '/home/user/Загрузки/Phyton/Pycharm_projects/Introduction-Python-12-2021/main_040122/test.json'
CSV_FILE_PATH = '/home/user/Загрузки/Phyton/Pycharm_projects/Introduction-Python-12-2021/main_040122/test.csv'
BAD_FILE_PATH = '/home/user/Загрузки/Phyton/Pycharm_projects/Introduction-Python-12-2021/main_040122/test.xxx'


def write_txt_file(file_path: str) -> None:
    with open(file_path, 'w') as txt_file:
        txt_file.write(get_rand_txt_str())


def write_csv_file(file_path: str) -> None:
    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(get_rand_csv_table())


def write_json_file(file_path: str) -> None:
    with open(file_path, 'w') as json_file:
        json.dump(get_rand_json_dict(), json_file)


def generate_and_write_file(file_path: str) -> None:
    file_ext = file_path.split('.')[-1]
    if file_ext == 'txt':
        write_txt_file(file_path)
    elif file_ext == 'json':
        write_json_file(file_path)
    elif file_ext == 'csv':
        write_csv_file(file_path)
    else:
        print('Unsupported file format')


generate_and_write_file(TXT_FILE_PATH)
generate_and_write_file(JSON_FILE_PATH)
generate_and_write_file(CSV_FILE_PATH)
generate_and_write_file(BAD_FILE_PATH)
