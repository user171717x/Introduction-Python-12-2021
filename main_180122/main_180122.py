"""
data.json - файл с данными о некоторых математиках прошлого.
1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
Если фамилии нет, то использовать имя, например Euclid.
3. Написать функцию сортировки по дате смерти из поля "years".
Обратите внимание на сокращение BC. - это означает до н.э.
4. Написать функцию сортировки по количеству слов в поле "text"
5. Написать функцию для записи отсортированных данных в файл. Параметры - имя файла для записи, параметр сортировки.
Пример использования:
write_json("new_data.json", "text")
"""

import json
import re


JSON_UNSORTED = 'data.json'
JSON_SORTED_TEXT = 'text.json'
JSON_SORTED_NAME = 'name.json'
JSON_SORTED_YEARS = 'years.json'


def read_json(file_name: str) -> list:
    """
    Read list with dictionaries from json file
    :param file_name: json file name
    :return: list with dictionaries
    """
    with open(file_name, 'r') as json_file:
        return json.load(json_file)


def write_json(file_name: str, sort_type: str) -> int:
    """
    Write json file with sorted dictionary list
    :param file_name: json file name
    :param sort_type: type of sorting: "name" - by lastname, "years" - by date of death,
     "text" - by number of words in the field text
    :return: int codes: 0 - file created success, 1 - any error, file not created
    """
    if sort_type == "years":
        write_data = sorted(data, key=sort_by_years)
    elif sort_type == "name":
        write_data = sorted(data, key=lambda x: x['name'].split()[-1])
    else:
        write_data = sorted(data, key=lambda x: len(x['text'].split()))
    try:
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(write_data, json_file, indent=2, ensure_ascii=False)    # to prevent write symbols as utf codes
        return 0
    except OSError:
        return 1


def sort_by_years(item):
    """
    Sort function, sorting dictionaries by date of death
    :param item: dictionary with mathematic's life description
    :return: date of death
    """
    years_line = item['years']
    death_year = int(re.findall(r"[0-9]+", years_line)[-1])
    return -death_year if years_line.count('BC') else death_year


data = read_json(JSON_UNSORTED)
write_json(JSON_SORTED_TEXT, "text")
write_json(JSON_SORTED_NAME, "name")
write_json(JSON_SORTED_YEARS, "years")
