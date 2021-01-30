def leap_year(x):
    """
    Check if a year is a leap year.
    A leap year in the Gregorian calendar occurs:
    - on every year that is evenly divisible by 4
    - except every year that is evenly divisible by 100
    - unless the year is also evenly divisible by 400
    """
    return x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)