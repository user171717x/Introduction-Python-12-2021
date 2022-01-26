
from event import Event
from argparse import ArgumentParser


"""
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
"""

args = ArgumentParser()
args.add_argument("event", type=str)
args.add_argument("amount", nargs='?', type=str, default='')

game = Event(*vars(args.parse_args()).values())
game.go()
