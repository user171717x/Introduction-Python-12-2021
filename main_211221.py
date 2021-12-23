
import random
import string


def list_scrap_start_a(work_list):
    res_list = [item for item in work_list if item.find('a') == 0]
    return res_list


def list_scrap_any_a(work_list):
    res_list = [item for item in work_list if item.find('a') > -1]
    return res_list


def list_scrap_all_strings(work_list):
    res_list = [item for item in work_list if type(item) is str]
    return res_list


def get_single_symbols(work_str):
    res_list = [symbol for symbol in work_str if work_str.count(symbol) == 1]
    return res_list


def get_crossed_symbols(string_1, string_2):
    res_list = list(set(string_1).intersection(set(string_2)))
    return res_list


def get_crossed_single_symbols(string_1, string_2):
    temp_list_1 = get_single_symbols(string_1)
    temp_list_2 = get_single_symbols(string_2)
    res_list = list(set(temp_list_1).intersection(set(temp_list_2)))
    return res_list


def create_email(list_domains, list_lastnames):
    domain_address_min_len = 5
    domain_address_max_len = 7
    random.seed()
    letters = string.ascii_lowercase  # all abc lowercase letters
    string_length = random.randint(domain_address_min_len, domain_address_max_len)  # string have random length
    # creating string from letters using loop with our length
    domain_address = ''.join(random.choice(letters) for _ in range(string_length))

    result = f"{random.choice(list_lastnames)}.{random.randint(100, 999)}@{domain_address}.{random.choice(list_domains)}"
    return result


"""
1. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list у которых первый символ - буква "a".
"""
my_list_1 = ['', 'hello', '2344', 'allo', 'OllA', 'tomas', '56batter', 'Ato', 'arrow']
print(list_scrap_start_a(my_list_1))

"""
2. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list в которых есть символ - буква "a" на любом месте.
"""
print(list_scrap_any_a(my_list_1))

"""
3. Написать функцию которой передается один параметр - список строк my_list в
котором могут быть как строки (type str) так и целые числа (type int).
Например [1, 2, 3, "11", "22", 33, "one"]
Функция возвращает новый список в котором содержаться только строки из my_list.
"""
my_list_2 = [1, 2, 3, "11", "22", 33, "one"]
print(list_scrap_all_strings(my_list_2))

"""
4. Написать функцию которой передается один параметр - строка my_str.
Функция возвращает список в котором содержаться те символы из my_str,
которые встречаются в строке только один раз.
Т.е. для строкb "qqweeerrty" ответ должен быть ["w", "t", "y"]
"""
my_str_1 = "qqweeerrty"
print(get_single_symbols(my_str_1))

"""
5. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
Т.е. для строк "qqwwerrttyy" и "qweeeeeee123" ответ должен быть ["q", "w", "e"]
"""
my_str_2 = "qqwwerrttyy"
my_str_3 = "qweeeeeee123"
print(get_crossed_symbols(my_str_2, my_str_3))

"""
6. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
Т.е. для строк "qwwwwerrrrtyyyy" и "qweeeeeeerty123" ответ должен быть ["q", "t"]
"""
my_str_4 = "qwwwwerrrrtyyyy"
my_str_5 = "qweeeeeeerty123"
print(get_crossed_single_symbols(my_str_4, my_str_5))

"""
7*. Даны списки names и domains (создать самостоятельно).
Написать функцию create_email для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.

Пример использования функции:
names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)
>>>miller.249@sgdyyur.com

"""
lastnames = ["king", "miller", "kean", "dodge", "lord", "bustard", "gongadze", "bills"]
domains = ["net", "com", "ua", "co", "su", "dp", "domain"]
e_mail = create_email(domains, lastnames)
print(e_mail)
