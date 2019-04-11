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
# populate month values
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
assert len(months) == 12
class Months:
    @staticmethod
    def from_index(i):
        for m in months:
            if getattr(Months, m) == i:
                return m
        return -1
for i, month in enumerate(months):
    setattr(Months, month, i+1) # start from 1 to correctly index

# populate day values
days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
assert len(days) == 7
class Days:
    @staticmethod
    def from_index(i):
        for d in days:
            if getattr(Days, d) == i:
                return d
        return -1
for i, day in enumerate(days):
    setattr(Days, day, i+1)

# jan 1 1900 Monday
base = {
    'day': 1,
    'month': 1, # 1 based index
    'year': 1900,
    'weekday': 2 # mon=2
}

database = []

def calculate_days_until(month, year):
    # starts at Janurary
    dayweek = 2
    years = year - base['year']
    months = years * 12 + month
    dayweeks = []
    for y in range(year, year+years+1):
        for m in range(months):
            m = (m%12) + 1
            for d in range(number_of_days_in_month(m, y)):
                print(y, m, Months.from_index(m), d+1, dayweek, Days.from_index(dayweek))
                dayweek = (dayweek % 7) + 1
                # year, month, monthname, day, dayweek, dayweekname len=6 index=0
                dayweeks.append((y, m, Months.from_index(m), d+1, dayweek, Days.from_index(dayweek)))
    return dayweeks

def calculate_sundays_from_until(start, end):
    dayweek = 2
    month1, year1 = start
    month2, year2 = end
    years = year2 - year1
    dayweeks = []
    if years == 0:
        months = month2 - month1 + 1
    else:
        months = 13 - month1 + month2 + (max(0, years - 2)) * 12
    for y in range(year1, year1+years+1):
        for m in range(months):
            m = (m%12) + 1
            for d in range(number_of_days_in_month(m, y)):
                dayweek = (dayweek % 7) + 1
                if dayweek == 7:
                    print(y, m, Months.from_index(m), d+1, dayweek, Days.from_index(dayweek))
                    dayweeks.append((y, m, Months.from_index(m), d+1, dayweek, Days.from_index(dayweek)))

def number_of_days_in_month(month, year):
    if not 0 < month < 13:
        raise ValueError(f"Month value should be between 1-3: Got {month}")
    # months are zero based indexed so month + 1 = actual month index
    # february = 1
    if month == 2:
        leap_year = year % 4 == 0
        leap_century = year % 400 == 0
        return 29 if leap_year and leap_century else 28
    elif month in (4, 6, 9, 11):
        return 30
    return 31
    pass

# print(calculate_days_until(1, 1900))
print(calculate_sundays_from_until((1, 1900), (2, 1900)))