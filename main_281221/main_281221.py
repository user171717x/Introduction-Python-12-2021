
import calendar


# Delim logiky programmi, sozdali otdelnyu fynkciu kotoraya ispolzyetsya kagdoi drygoi fynkciey
def read_file(filename):
    with open(filename, 'r') as txt_file:
        data = txt_file.read()
        data = data.split('\n') # delim txt file na stroki
    return data


def get_domains_list(file_name: str) -> list:
    lines = read_file(file_name)
    domains = [line.replace('.', '') for line in lines]
    return domains
    # with open(file_name, 'r') as text_file:
    #     text = text_file.read().strip('.')
    # return text.split('\n.')


def get_lastnames_list(file_name: str) -> list:
    lines = read_file(file_name)
    names = [line.split('\t')[1] for line in lines]
    return names
    # with open(file_name, 'r') as text_file:
    #     text = text_file.readlines()
    # return [line.split('\t')[1] for line in text]


def convert_date(date_str: str) -> str:
    ## GOT FROM ## commented lines
    ## month_dict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05',
    ##               'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10',
    ##              'November': '11', 'December': '12'}
    month_dict = {month: str(idx).zfill(2) for idx, month in enumerate(calendar.month_name) if month}
    day, month, year = date_str.split()
    day = day[:-2].zfill(2)
    month = month_dict[month]
    return f"{day}/{month}/{year}"
    # months = calendar.month_name[:]
    # date_fields = date_str.split()
    # day_year = date_fields[2]
    # day_month = str(months.index(date_fields[1])).zfill(2)  # adding needed 0 at start
    # day_day = date_fields[0][:-2].zfill(2)
    # return f"{day_day}/{day_month}/{day_year}"


def scrap_dates(filename):
    authors = []
    lines = read_file(filename)
    ##count = 1
    ##month_dict = {}
    for line in lines:
        if ' - ' in line:
            date_author = line.split(' - ')[0]
            authors.append({"data_original": date_author, "data_modified": convert_date(date_author)})
        ##elif ' - ' not in line and line:    # 2nd yslovie - oznachaet NE PYSTAYA STROKA
        ##    month_dict[line] = str(count).zfill(2)
        ##   count += 1
    ##print(month_dict)
    return authors
# def scrap_date_lines(file_name: str) -> list:
#     with open(file_name, 'r') as text_file:
#         text = text_file.readlines()
#     date_lines = list()
#     for line in text:
#         if ' - ' in line:
#             date_lines.append(line.split(' - ')[0])
#     return date_lines
# def scrap_dates(file_name: str) -> list:
#     return [{'date_original': date, 'date_modified': convert_date(date)} for date in scrap_date_lines(file_name)]


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
