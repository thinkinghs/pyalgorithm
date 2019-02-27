# calendar api
# https://docs.python.org/3/library/calendar.html

from calendar import day_name, weekday

input_value = input().split(' ')
year = int(input_value[2])
month = int(input_value[0])
day = int(input_value[1])

print(day_name[weekday(year,month,day)].upper())
