
import calendar


def get_domains_list(file_name: str) -> list:
    with open(file_name, 'r') as text_file:
        text = text_file.read().strip('.')
    return text.split('\n.')


def get_lastnames_list(file_name: str) -> list:
    with open(file_name, 'r') as text_file:
        text = text_file.readlines()
    return [line.split('\t')[1] for line in text]


def convert_date(date_str: str) -> str:
    months = calendar.month_name[:]
    date_fields = date_str.split()
    day_year = date_fields[2]
    raw_month = months.index(date_fields[1])
    raw_day = date_fields[0][:-2]
    day_month = raw_month if int(raw_month) > 9 else '0' + str(raw_month)
    day_day = raw_day if int(raw_day) > 9 else '0' + str(raw_day)
    return f"{day_day}/{day_month}/{day_year}"


def scrap_dates(file_name: str) -> list:
    with open(file_name, 'r') as text_file:
        text = text_file.readlines()
    date_lines = list()
    for line in text:
        if line.count('-'):
            date_lines.append(line[:line.index('-') - 1])

    result = list()
    for date in date_lines:
        date_dict = dict()
        date_dict['date_original'] = date
        date_dict['date_modified'] = convert_date(date)
        result.append(date_dict)

    return result


"""
1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
и возвращает их в виде списка строк (названия возвращать без точки).

"""
print(get_domains_list('domains.txt'))


"""
2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
и возвращает список всех фамилий из него.
Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
Разделитель - символ табуляции "\t"
"""
print(get_lastnames_list('names.txt'))


"""
3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
словарей вида {"date_original": date_original, "date_modified": date_modified}
в которых date_original - это дата из строки (если есть),
а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
"""
print(scrap_dates('authors.txt'))
