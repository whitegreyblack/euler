# problem 19
# counting sundays

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
assert len(months) == 12

def days_in_month(month, year):
    # february
    if month == 2:
        leap_year = year % 4 == 0
        leap_century = year % 400 == 0
        return 29 if leap_year and leap_century else 28
    elif month in (4, 6, 9, 11):
        return 30
    return 31

# jan 1 1900 Monday
# jan 7 1900 Sunday
def get_sundays_in_month(month, year):
    pass

print(days_in_month(2, 1900))
print(days_in_month(2, 2000))