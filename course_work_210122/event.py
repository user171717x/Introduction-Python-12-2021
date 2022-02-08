import csv
import json
import random


class Event:
    def __init__(self, event, amount):
        self._start_config = 'config.json'  # config file with initial conditions and exchange rate change delta
        self._history_file = 'history.csv'  # table with game state changes

        with open(self._start_config, 'r') as json_file:
            self.__game_config = json.load(json_file)
        with open(self._history_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            self.__game_data = list(reader)[-1]

        self._event = event
        self._amount = amount
        self.__encryption = self.__game_config['encrypt']

        if event == 'RESTART':
            self.__restart()
            self.__save('w')
        if self.__game_data['event'] != 'RESTART':
            self.__decrypt()

        self.__exchange_rate = float(self.__game_data['exchange_rate'])
        self.__uah_total = float(self.__game_data['uah_total'])
        self.__usd_total = float(self.__game_data['usd_total'])
        self.__delta = float(self.__game_config['delta'])

    def go(self):
        if self._event == 'RATE':
            self.__rate()
        elif self._event == 'AVAILABLE':
            self.__available()
        elif self._event == 'RESTART':
            self.__restart()
        elif self._event == 'NEXT':
            self.__next()
        elif self._event == 'BUY':
            if self._amount == 'ALL':
                self.__buy_all()
            else:
                self.__buy(float(self._amount))
        elif self._event == 'SELL':
            if self._amount == 'ALL':
                self.__sell_all()
            else:
                self.__sell(float(self._amount))

        if self._event == 'RESTART':
            self.__save('w')
        else:
            self.__save()

    def __save(self, open_status='a') -> None:
        """
        Refresh state file in case Restart event or adding current game state to history file
        :param open_status: 'a' - adding line to history, 'w' - rewrite history after restart game
        :return: None
        """
        self.__game_data['exchange_rate'] = str(self.__exchange_rate)
        self.__game_data['uah_total'] = str(self.__uah_total)
        self.__game_data['usd_total'] = str(self.__usd_total)
        self.__game_data['event'] = self._event
        if open_status == 'a':
            self.__encrypt()
        with open(self._history_file, open_status, encoding='utf-8') as csv_file:
            fieldnames = self.__game_data.keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if open_status == 'w':
                writer.writeheader()
            writer.writerow(self.__game_data)

    def __restart(self) -> None:
        """
        Start new game with initial conditions , restart history table
        :return: None
        """
        self.__exchange_rate = float(self.__game_config['exchange_rate'])
        self.__uah_total = float(self.__game_config['uah_total'])
        self.__usd_total = float(self.__game_config['usd_total'])

    def __rate(self) -> None:
        """
        Display current exchange rate
        :return: None
        """
        print(self.__exchange_rate)

    def __available(self) -> None:
        """
        Display current available balances
        :return: None
        """
        print(f"USD {self.__uah_total} UAH {self.__usd_total}")

    def __next(self) -> None:
        """
        Generate next exchange rate
        :return: None
        """
        self.__exchange_rate = str(
            random.randint(
                int(self.__exchange_rate * 100 - self.__delta * 100),
                int(self.__exchange_rate * 100 + self.__delta * 100))
            / 100
        )

    def __buy(self, amount: float) -> None:
        """
        Buy XXX dollars.
        In case if there is no enough UAH for purchase - display message like:
        UNAVAILABLE, REQUIRED BALANCE UAH 2593.00, AVAILABLE 1000.00
        :param amount: amount of dollars to buy
        :return: None
        """
        require_uah = round(amount * self.__exchange_rate, 2)
        if self.__uah_total >= require_uah:
            self.__usd_total += amount
            self.__uah_total -= require_uah
            self._event = f"BUY {amount} DONE"
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {require_uah}, AVAILABLE {self.__uah_total}")
            self._event = f"BUY {amount} CANCELLED"

    def __buy_all(self) -> None:
        """
        Buy dollars for all available hryvnias
        :return: None
        """
        expect_usd = round(self.__uah_total / self.__exchange_rate, 2)
        pay_uah = (expect_usd - 0.01) * self.__exchange_rate
        self.__uah_total = round(self.__uah_total - pay_uah, 2)
        self.__usd_total = round(self.__usd_total + pay_uah / self.__exchange_rate, 2)
        self._event = 'BUY ALL'

    def __sell(self, amount: float) -> None:
        """
        Sell XXX dollars.
        In case if there is no enough USD for purchase - display message like:
        UNAVAILABLE, REQUIRED BALANCE USD 200.00, AVAILABLE 135.00
        :param amount: amount of dollars to sell
        :return: None
        """
        if self.__usd_total >= amount:
            self.__usd_total -= amount
            self.__uah_total = round(self.__uah_total + amount * self.__exchange_rate, 2)
            self._event = f"SELL {amount} DONE"
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount}, AVAILABLE {self.__usd_total}")
            self._event = f"SELL {amount} CANCELLED"

    def __sell_all(self) -> None:
        """
        Sell all dollars
        :return: None
        """
        self.__uah_total = round(self.__uah_total + self.__usd_total * self.__exchange_rate, 2)
        self.__usd_total = 0.0
        self._event = 'SELL ALL'

    def __encrypt(self) -> None:
        """
        Basic encrypt of game state dictionary to prevent simple falsification
        "encrypt": 1 at config - encrypt game data, "encrypt": 0 - game data without encrypt
        :return: None
        """
        if self.__encryption:
            self.__game_data = {key: "".join([f" {ord(symbol) ** 2}" for symbol in self.__game_data[key]]) for key in
                                self.__game_data.keys()}

    def __decrypt(self) -> None:
        """
        Decrypt encrypted game state dictionary
        "encrypt": 1 at config - game data encrypted, "encrypt": 0 - game data without encrypt
        :return: None
        """
        if self.__encryption:
            self.__game_data = {key: "".join([chr(int(int(symbol) ** 0.5)) for symbol in self.__game_data[key].split()])
                                for key in
                                self.__game_data.keys()}


print("hello")