import calendar

year = 2023

for month in range(1, 13):
    x = calendar.month(year, month)
    print(x, end=' ')
