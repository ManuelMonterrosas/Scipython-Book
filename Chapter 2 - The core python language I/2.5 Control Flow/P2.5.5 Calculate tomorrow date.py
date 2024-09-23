"""
Write a program to determine tomorrow’s date given a string representing
today’s date, today, as either “D/M/Y” or “M/D/Y”. Cater for both British and US-style
dates when parsing today according to the value of a boolean variable us_date_style.
For example, when us_date_style is False and today is '3/4/2014', tomorrow’s date
should be reported as '4/4/2014'.25 (Hint: use the algorithm for determining if a year
is a leap year, which is provided in the example to Section 2.5.1.)
"""

def is_leap_year(year):
    if not year % 400:
        answer = True
    elif not year % 100:
        answer = False
    elif not year % 4:
        answer = True
    else:
        answer = False
    return answer

today_date = '31/12/2020'  # I'm assuming dates are given nicely. Otherwise I need ifs and trys
us_date_style = False

if us_date_style:
    month, day, year = today_date.split('/')
else:
    day, month, year = today_date.split('/')

day = int(day)
month = int(month)
year = int(year)

month_names = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
max_days = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # the maximum days per month
if is_leap_year(year):
    max_days[2] += 1

# Calculate tomorrow's date
tw_day = day + 1
tw_month = month
tw_year = year 
if tw_day > max_days[month]:
    tw_day = 1
    tw_month += 1
    if tw_month > 12:
        tw_month = 1
        tw_year += 1
    
print("Today is", month_names[month], "{:02d}, {:4d}".format(day, year))
print("Tomorrow is", month_names[tw_month], "{:02d}, {:4d}".format(tw_day, tw_year))
