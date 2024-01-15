# Dates - Fechas y horas
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/16_Day_Python_date_time/16_python_datetime.md
"""import datetime
 print(dir(datetime)) # ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo'] """

# Obteniendo información datetime
""" from datetime import datetime
now = datetime.now()            
print(now)                      # 2024-01-15 07:55:23.305204
day = now.day                   # 15
month = now.month               # 1
year = now.year                 # 2024
hour = now.hour                 # 7
minute = now.minute             # 55
second = now.second
timestamp = now.timestamp()     
print(day, month, year, hour, minute) # 15 1 2024 7 55
print('timestamp', timestamp)   # timestamp 1705323323.305204
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 15/1/2024, 7:55 """

# Formateando salida de fecha usando strftime
""" from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0 """

# using strftime method
""" from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S") # time: 08:02:15
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one) # time one: 01/15/2024, 08:02:15
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two) # time two: 15/01/2024, 08:02:15 """

# String to Time Using strptime
""" from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string) # date_string = 5 December, 2019
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object) # date_object = 2019-12-05 00:00:00 """

# Using date from datetime
""" from datetime import date
d = date(2020, 1, 1)
print(d)                             # 2020-01-01
print('Current date:', d.today())    # Current date: 2024-01-15
# date object of today's date
today = date.today()
print("Current year:", today.year)   # Current year: 2024
print("Current month:", today.month) # Current month: 1
print("Current day:", today.day)     # Current day: 15 """

# Time Objects to Represent Time
""" from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)  
print("b =", b)     # b = 10:30:50  
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555 """

# Difference Between Two Points in Time Using
""" from datetime import time, date, datetime
today = date(year=2024, month=1, day=15)
new_year = date(year=2025, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  352 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2024, month = 1, day = 15, hour = 8, minute = 21, second = 0)
t2 = datetime(year = 2025, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00 """

# Difference Between Two Points in Time Using timedelta
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)