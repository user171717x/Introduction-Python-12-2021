import csv
import json
import random
from argparse import ArgumentParser

START_CONFIG = 'config.json'    # config file with initial conditions and exchange rate change delta
HISTORY_FILE = 'history.csv'    # table with game state changes


def event_listener() -> None:
    """
    Main function, getting arguments from command line and run events

    Arguments table:
    RATE - current exchange rate (USD/UAH)
    AVAILABLE - available balances
    BUY XXX - buy XXX dollars. In case if there is no enough UAH for purchase - display message like:
                                                        UNAVAILABLE, REQUIRED BALANCE UAH 2593.00, AVAILABLE 1000.00
    SELL XXX - sell XXX dollars. In case if there is no enough USD for purchase - display message like:
                                                        UNAVAILABLE, REQUIRED BALANCE USD 200.00, AVAILABLE 135.00
    BUY ALL - buy dollars for all available hryvnias
    SELL ALL - sell all dollars
    NEXT - get next exchange rate
    RESTART - start the new game (with initial conditions)

    :return: None
    """
    args = ArgumentParser()
    args.add_argument("event", type=str)
    args.add_argument("amount", nargs='?', type=str, default='')
    event, amount = vars(args.parse_args()).values()
    if event == 'RATE':
        event_rate()
    elif event == 'AVAILABLE':
        event_available()
    elif event == 'RESTART':
        event_restart()
    elif event == 'NEXT':
        event_next()
    elif event == 'BUY':
        if amount == 'ALL':
            event_buy_all()
        else:
            event_buy(float(amount))
    elif event == 'SELL':
        if amount == 'ALL':
            event_sell_all()
        else:
            event_sell(float(amount))


def open_event() -> dict:
    """
    Get current game state from HISTORY_FILE
    :return: dictionary with game state
    """
    with open(HISTORY_FILE, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        game_data = list(reader)[-1]
    return game_data if game_data['event'] == 'RESTART' else decrypt(game_data)


def save_event(game_data: dict, open_status: str = 'a') -> None:
    """
    Refresh state file in case Restart event or adding current game state to history file
    :param open_status: 'a' - adding line to history, 'w' - rewrite history after restart game
    :param game_data: dictionary with game state
    :return: None
    """
    if open_status == 'a':
        game_data = encrypt(game_data)
    with open(HISTORY_FILE, open_status, encoding='utf-8') as csv_file:
        fieldnames = game_data.keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if open_status == 'w':
            writer.writeheader()
        writer.writerow(game_data)


def event_restart() -> None:
    """
    Start new game with initial conditions , restart history table
    :return: None
    """
    with open(START_CONFIG, 'r') as json_file:
        game_data = json.load(json_file)
    game_data['event'] = 'RESTART'
    del game_data['delta']
    del game_data['encrypt']

    save_event(game_data, 'w')


def event_rate() -> None:
    """
    Display current exchange rate
    :return: None
    """
    game_data = open_event()

    print(game_data['exchange_rate'])
    game_data['event'] = 'RATE'

    save_event(game_data)


def event_available() -> None:
    """
    Display current available balances
    :return: None
    """
    game_data = open_event()

    print(f"USD {game_data['usd_total']} UAH {game_data['uah_total']}")
    game_data['event'] = 'AVAILABLE'

    save_event(game_data)


def event_next() -> None:
    """
    Generate next exchange rate
    :return: None
    """
    game_data = open_event()

    with open(START_CONFIG, 'r') as json_file:
        config_data = json.load(json_file)

    current_rate = float(game_data['exchange_rate'])
    delta = float(config_data['delta'])
    new_rate = random.randint(int(current_rate * 100 - delta * 100), int(current_rate * 100 + delta * 100)) / 100
    game_data['exchange_rate'] = str(new_rate)
    game_data['event'] = 'NEXT'

    save_event(game_data)


def event_buy(amount: float) -> None:
    """
    Buy XXX dollars.
    In case if there is no enough UAH for purchase - display message like:
    UNAVAILABLE, REQUIRED BALANCE UAH 2593.00, AVAILABLE 1000.00
    :param amount: amount of dollars to buy
    :return: None
    """
    game_data = open_event()

    amount_uah = float(game_data['uah_total'])
    amount_usd = float(game_data['usd_total'])
    exchange_rate = float(game_data['exchange_rate'])
    expect_usd = float(amount)
    require_uah = round(amount * exchange_rate, 2)

    if amount_uah >= require_uah:
        amount_usd += expect_usd
        amount_uah -= require_uah
        game_data['event'] = f"BUY {amount} DONE"
        game_data['uah_total'] = str(round(amount_uah, 2))
        game_data['usd_total'] = str(round(amount_usd, 2))
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {require_uah}, AVAILABLE {amount_uah}")
        game_data['event'] = f"BUY {amount} CANCELLED"

    save_event(game_data)


def event_buy_all() -> None:
    """
    Buy dollars for all available hryvnias
    :return: None
    """
    game_data = open_event()

    amount_uah = float(game_data['uah_total'])
    amount_usd = float(game_data['usd_total'])
    exchange_rate = float(game_data['exchange_rate'])
    expect_usd = round(amount_uah / exchange_rate, 2)
    pay_uah = (expect_usd - 0.01) * exchange_rate
    get_usd = pay_uah / exchange_rate
    amount_uah -= pay_uah
    amount_usd += get_usd
    game_data['event'] = 'BUY ALL'
    game_data['uah_total'] = str(round(amount_uah, 2))
    game_data['usd_total'] = str(round(amount_usd, 2))

    save_event(game_data)


def event_sell(amount: float) -> None:
    """
    Sell XXX dollars.
    In case if there is no enough USD for purchase - display message like:
    UNAVAILABLE, REQUIRED BALANCE USD 200.00, AVAILABLE 135.00
    :param amount: amount of dollars to sell
    :return: None
    """
    game_data = open_event()

    amount_uah = float(game_data['uah_total'])
    amount_usd = float(game_data['usd_total'])
    exchange_rate = float(game_data['exchange_rate'])
    require_usd = float(amount)
    receive_uah = round(amount * exchange_rate, 2)

    if amount_usd >= require_usd:
        amount_usd -= require_usd
        amount_uah += receive_uah
        game_data['event'] = f"SELL {amount} DONE"
        game_data['uah_total'] = str(round(amount_uah, 2))
        game_data['usd_total'] = str(round(amount_usd, 2))
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {require_usd}, AVAILABLE {amount_usd}")
        game_data['event'] = f"SELL {amount} CANCELLED"

    save_event(game_data)


def event_sell_all() -> None:
    """
    Sell all dollars
    :return: None
    """
    game_data = open_event()

    amount_uah = float(game_data['uah_total'])
    amount_usd = float(game_data['usd_total'])
    exchange_rate = float(game_data['exchange_rate'])
    get_uah = amount_usd * exchange_rate
    amount_usd = 0.0
    amount_uah += get_uah
    game_data['event'] = 'SELL ALL'
    game_data['uah_total'] = str(round(amount_uah, 2))
    game_data['usd_total'] = str(amount_usd)

    save_event(game_data)


def encrypt(game_data: dict) -> dict:
    """
    Basic encrypt of game state dictionary to prevent simple falsification
    "encrypt": 1 at config - encrypt game data, "encrypt": 0 - game data without encrypt
    :param game_data: dictionary with game state
    :return: encrypted dictionary with game state
    """
    with open(START_CONFIG, 'r') as json_file:
        game_config = json.load(json_file)
    if game_config['encrypt']:
        return {key: "".join([f" {ord(symbol) ** 2}" for symbol in game_data[key]]) for key in game_data.keys()}
    else:
        return game_data


def decrypt(game_data: dict) -> dict:
    """
    Decrypt encrypted game state dictionary
    "encrypt": 1 at config - game data encrypted, "encrypt": 0 - game data without encrypt
    :param game_data: encrypted dictionary with game state
    :return: dictionary with game state
    """
    with open(START_CONFIG, 'r') as json_file:
        game_config = json.load(json_file)
    if game_config['encrypt']:
        return {key: "".join([chr(int(int(symbol) ** 0.5)) for symbol in game_data[key].split()]) for key in game_data.keys()}
    else:
        return game_data


event_listener()
