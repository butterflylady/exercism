def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError("Irregular matrix!")
    saddle_points = []
    for i in range(0, len(matrix)):
        max_row_val = max(matrix[i])
        max_row_val_col_index = [i for i, x in enumerate(matrix[i]) if x == max_row_val]
        for j in max_row_val_col_index:
            if min([row[j] for row in matrix]) == max_row_val:
                saddle_points.append({"row": i + 1, "column": j + 1})
    return saddle_points


"""
def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError("Wrong shape")

    points = []
    for i, row in enumerate(matrix):
        for j, number in enumerate(row):
            if number == max(row) and number == min([row[j] for row in matrix]):
                points.append({"row": i + 1, "column": j + 1})

    return points
"""