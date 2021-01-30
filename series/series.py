def slices(series, length):
    output = [series[i:i + length] for i in range(0, len(series) - length + 1)]
    if length > len(series):
        raise ValueError("The length of a substring is greater than the length of a string.")
    if length <= 0:
        raise ValueError("The length of a substring should be greater than 0.")
    return output