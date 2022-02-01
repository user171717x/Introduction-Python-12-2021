import datetime


def days_diff(a, b):
    diff = abs(datetime.date(*a) - datetime.date(*b))
    return diff.days

print(days_diff((1982, 4, 19), (1982, 4, 22)))


"""
Best "Clear" Solution:

from datetime import datetime

def days_diff(date1, date2):
    return abs((datetime(*date1)-datetime(*date2)).days)
"""


"""
Best "Speedy" Solution:

from datetime import date, timedelta
def days_diff(date1, date2):
   f=date(*date1)
   b=date(*date2)
   a=(f-b).days
   return abs(a)

"""