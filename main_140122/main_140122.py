
import csv
import requests
import random


def get_quote() -> dict:
    """
    Get 1 random quote from http://forismatic.com/ru/api/
    :return: dict with quote, in case with bad connection return {'quoteAuthor': ''}
    """
    url = 'http://api.forismatic.com/api/1.0/'
    params = {"method": "getQuote",
              "format": "json",
              "lang": "ru",
              "key": random.randint(1, 999999)}
    try:
        response = requests.get(url, params=params)
        response = response.json()
    except Exception:
        response = {'quoteAuthor': ''}
        print('Connection failed. Check internet connection!')
    return response


def get_signed_quote() -> dict:
    """
    Get 1 signed quote from http://forismatic.com/ru/api/ (using get_quote() function)
    :return: dict with quote (Author, Quote, URL)
    """
    while True:
        quote = get_quote()
        if quote['quoteAuthor'] == '':
            continue
        else:
            quote['Author'] = quote['quoteAuthor']
            quote['Quote'] = quote['quoteText']
            quote['URL'] = quote['quoteLink']
            del quote['quoteAuthor']
            del quote['quoteText']
            del quote['quoteLink']
            del quote['senderName']
            del quote['senderLink']
            return quote


def fetch_progress(total: int, current: int) -> None:
    if current == 1:
        print('Quotes fetch progress: ', end='')
    if not int((current / total) * 100 % 5):
        print('.', end='')
    if current == total:
        print(' Done')


def get_quotes(amount: int) -> list:
    """
    Getting quotes from http://forismatic.com/ru/api/ (using get_signed_quote() function)
    :param amount: the number of quotes
    :return: list of non-repeated quotes (if the author is not listed, do not quote)
    """
    result = list()
    while len(result) < amount:
        quote = get_signed_quote()
        if quote in result:
            continue
        else:
            result.append(quote)
            fetch_progress(amount, len(result))
    return result


def write_quotes_csv(quotes_list: list, file_name: str = 'quotes.csv') -> int:
    """
    Get list of quotes from get_quotes() and save it to csv file with headers: Author, Quote, URL
    Quotes sorted by author name (in alphabetical order)
    :param quotes_list: list with quotes, result of function get_quotes()
    :param file_name: csv file name to save quotes (default file name: 'quotes.csv')
    :return: int codes: 0 - file with quotes created success, 1 - any error, file not created
    """

    quotes_list.sort(key=str)

    try:
        with open(file_name, 'w', encoding='utf-8') as csv_file:
            fieldnames = quotes_list[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(quotes_list)
        return 0
    except OSError:
        return 1


AMOUNT = 20  # number of quotes to write to csv file

print(write_quotes_csv(get_quotes(AMOUNT)))
