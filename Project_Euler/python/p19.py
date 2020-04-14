
import os
'''
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
'''
#Jan31 FebS Mar31 A30 M31 June30 J31 A30 S30 N30 O31 D31
months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,
          11:30, 12:31, 13:29}
def is_leap_year(year):
    val = False
    if year & 3 == 0:
        val = True
    if year % 100 == 0:
        val = False
        if year % 400 == 0:
            val = True
    return val

def pe_19(endyear):
    day = 7#first Sunday
    year = 1900
    month = 1
    key = int(0)
    Sundays = int(0)
    while year < endyear:
        month = 1
        while month < 13:
            if month == 2 and is_leap_year(year):
                key = 13
            else:
                key = month
            while day < months[key]:
                day += 7
            day = day % months[key]
            if day == 1:
                Sundays += 1
            month += 1
        year += 1
    return Sundays
       
if __name__ == '__main__':
    print(pe_19(2001)-pe_19(1901))
