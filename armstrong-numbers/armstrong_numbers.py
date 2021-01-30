def is_armstrong_number(number):
    """
    Returns True if the number is an Armstrong number
    (a number that is the sum of its own digits each raised to the power of the number of digits).
    """
    digit_power = len(str(number))
    return number == sum([int(d) ** digit_power for d in str(number)])
