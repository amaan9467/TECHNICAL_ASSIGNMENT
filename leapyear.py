def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter a year: "))

print(f"{year} is a leap year" if is_leap_year(year) else f"{year} is not a leap year")