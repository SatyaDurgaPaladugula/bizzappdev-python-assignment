"""
Problem:
Calculate days between two dates.
"""
from datetime import datetime

def date_difference(date1, date2):
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")
    return abs((d2 - d1).days)


print("Days lived:", date_difference("25-04-2000", "25-04-2025"))

