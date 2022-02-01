import string
import csv
import json
import random

MIN_STR_LEN = 100
MAX_STR_LEN = 1000
MIN_DICT_LEN = 5
MAX_DICT_LEN = 20
KEY_DICT_LEN = 5
MIN_T_LIMIT = 3
MAX_T_LIMIT = 10

TXT_FILE_PATH = '/home/user/Загрузки/Phyton/Pycharm_projects/Introduction-Python-12-2021/main_280122/test.txt'
JSON_FILE_PATH = '/home/user/Загрузки/Phyton/Pycharm_projects/Introduction-Python-12-2021/main_280122/test.json'
CSV_FILE_PATH = '/home/user/Загрузки/Phyton/Pycharm_projects/Introduction-Python-12-2021/main_280122/test.csv'
BAD_FILE_PATH = '/home/user/Загрузки/Phyton/Pycharm_projects/Introduction-Python-12-2021/main_280122/test.xxx'


class RandStr:
    def __init__(self, length: int = 0, len_min: int = None, len_max: int = None,
                 letters: str = f"{string.ascii_letters}{string.digits}"):
        if length > 0:
            self.__min_str_len = length
            self.__max_str_len = length
        elif len_min and len_max:
            self.__min_str_len = len_min
            self.__max_str_len = len_max
        else:
            self.__min_str_len = length
            self.__max_str_len = length
        if self.__min_str_len < self.__max_str_len:
            self.__str_len = random.randint(self.__min_str_len, self.__max_str_len)
        else:
            self.__str_len = random.randint(self.__max_str_len, self.__min_str_len)
        self.__letters = letters
        self.__string = self._get_string()

    def __str__(self):
        return self.__string

    def _set_string(self, length: int = 0, len_min: int = None, len_max: int = None, letters: str = None):
        if length > 0:
            self.__min_str_len = length
            self.__max_str_len = length
            self.__str_len = length
        elif len_min and len_max:
            self.__min_str_len = len_min
            self.__max_str_len = len_max
            if self.__min_str_len < self.__max_str_len:
                self.__str_len = random.randint(self.__min_str_len, self.__max_str_len)
            else:
                self.__str_len = random.randint(self.__max_str_len, self.__min_str_len)
        self.__letters = letters if letters else self.__letters
        self.__string = self._get_string() if length or (len_min and len_max) or letters else self.__string

    def _get_string(self):
        self.__string = "".join(random.choice(self.__letters) for _ in range(self.__str_len))
        return self.__string


class RandDict:
    def __init__(self, len_min: int = MIN_DICT_LEN, len_max: int = MAX_DICT_LEN,
                 key_letters: str = string.ascii_lowercase):
        self.__min_dict_len = len_min
        self.__max_dict_len = len_max
        self.__key_letters = key_letters
        self._dictionary = self._get_dict()

    def __str__(self):
        return str(self._dictionary.items())

    def __get_key_value(self):
        res_int = random.randint(-100, 100)
        res_float = random.random()
        res_bool = random.choice([True, False])
        return random.choice([res_int, res_float, res_bool])

    def _get_dict(self):
        self._dictionary = {f"{RandStr(letters=self.__key_letters, length=KEY_DICT_LEN)}": self.__get_key_value()
                            for _ in range(random.randint(self.__max_dict_len, self.__max_dict_len))}
        return self._dictionary


class RandTable:
    def __init__(self, min_t_limit: int = MIN_T_LIMIT, max_t_limit: int = MAX_T_LIMIT):
        self.__n_rows = random.randint(min_t_limit, max_t_limit)
        self.__m_cells = random.randint(min_t_limit, max_t_limit)
        self._table = self._get_table()

    def __str__(self):
        return str(self._table)

    def _get_table(self):
        self._table = [[random.randint(0, 1) for _ in range(self.__m_cells)] for _ in range(self.__n_rows)]
        return self._table


class WriteTxt(RandStr):
    def __init__(self, file_path: str, length: int = 0, len_min: int = MIN_STR_LEN, len_max: int = MAX_STR_LEN,
                 letters: str = f"{string.ascii_letters}{string.digits}{string.whitespace[0]}"):
        super().__init__(length, len_min, len_max, letters)
        self.__file_path = file_path

    def _write(self):
        with open(self.__file_path, 'w') as txt_file:
            txt_file.write(self._get_string())


class WriteCsv(RandTable):
    def __init__(self, file_path: str, min_t_limit: int = MIN_T_LIMIT, max_t_limit: int = MAX_T_LIMIT):
        super().__init__(min_t_limit, max_t_limit)
        self.__file_path = file_path

    def _write(self):
        with open(self.__file_path, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self._get_table())


class WriteJson(RandDict):
    def __init__(self, file_path: str, len_min: int = MIN_DICT_LEN, len_max: int = MAX_DICT_LEN,
                 key_letters: str = string.ascii_lowercase):
        super().__init__(len_min, len_max, key_letters)
        self.__file_path = file_path

    def _write(self):
        with open(self.__file_path, 'w') as json_file:
            json.dump(self._get_dict(), json_file)


class GenAndWriteFile(WriteTxt, WriteCsv, WriteJson):
    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__file_ext = self.__file_path.split('.')[-1]
        if self.__file_ext == 'txt':
            WriteTxt.__init__(self, self.__file_path)
        elif self.__file_ext == 'json':
            WriteJson.__init__(self, self.__file_path)
        elif self.__file_ext == 'csv':
            WriteCsv.__init__(self, self.__file_path)

    def write(self):
        if self.__file_ext == 'txt':
            WriteTxt._write(self)
        elif self.__file_ext == 'json':
            WriteJson._write(self)
        elif self.__file_ext == 'csv':
            WriteCsv._write(self)
        else:
            print('Unsupported file format')

# Better >>>
# class GenAndWriteFile:
#     def init(self, file_path: str):
#         self.__file_path = file_path
#         self.__file_ext = self.__file_path.split('.')[-1]
#         if self.__file_ext == 'txt':
#             self.writer = WriteTxt(file_path)
#         elif self.__file_ext == 'json':
#             self.writer = WriteJson(file_path)
#         elif self.__file_ext == 'csv':
#             self.writer = WriteCsv(file_path)
#         else:
#             print('Unsupported file format')
#
#     def write(self):
#         self.writer._write(self)


GenAndWriteFile(TXT_FILE_PATH).write()
GenAndWriteFile(JSON_FILE_PATH).write()
GenAndWriteFile(CSV_FILE_PATH).write()
GenAndWriteFile(BAD_FILE_PATH).write()

