def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The sequences should be of the same length.")
    return sum([1 for i in range(0, len(strand_a)) if strand_a[i] != strand_b[i]])
