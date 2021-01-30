def is_valid(isbn):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    character = ["X"]
    isbn_list = [ch for ch in isbn if ch in digits + character]
    isbn_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "X": 10}
    if len(isbn_list) == 10 and set(isbn_list[0:9]).issubset(digits) and isbn_list[-1] in digits + character:
        sum = 0
        for i in range(0, len(isbn_list)):
            sum += (10 - i) * isbn_dict[isbn_list[i]]
    else:
        return False
    return sum % 11 == 0