def classify(number):
    if number > 0:
        factors_list = [f for f in range(1, number) if number % f == 0]
        if sum(factors_list) == number:
            return "perfect"
        if sum(factors_list) > number:
            return "abundant"
        if sum(factors_list) < number:
            return "deficient"
    else:
        raise ValueError("A number should be a natural number")
