import calendar
import re


def date_time(time: str) -> str:
    parts = list(map(int, re.findall(r'\d+', time)))
    return f"{parts[0]} {calendar.month_name[parts[1]]} {parts[2]} year {parts[3]} " \
           f"{'hour' if parts[3] == 1 else 'hours'} {parts[4]} {'minute' if parts[4] == 1 else 'minutes'}"


print(date_time("01.01.2000 00:00"))

"""
Best "Clear" Solution

from datetime import datetime

def checkio(time):
    dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    hour = 'hour' if dt.hour == 1 else 'hours'    
    minute = 'minute' if dt.minute == 1 else 'minutes'
    return dt.strftime(f'%-d %B %Y year %-H {hour} %-M {minute}')    
"""

"""
Best "Speedy" Solution


from datetime import datetime

def date_time(time: str) -> str:
    t=datetime.strptime(time,'%d.%m.%Y %H:%M')
    return t.strftime(f'%-d %B %Y year %-H hour{"s" if t.hour!=1 else ""} %-M minute{"s" if t.minute!=1 else ""}')

"""