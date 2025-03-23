def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

if month == 2:
    days = 29 if is_leap_year(year) else 28
elif month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
else:
    days = 30

print(f"The number of days is {days}")
