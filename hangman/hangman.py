# Game status categories
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.masked_word = "_" * len(word)
        self.char_pos_list = {}

    def guess(self, char):
        if self.get_status() == STATUS_ONGOING:
            if (char not in self.char_pos_list) and (char in self.word):
                self.char_pos_list[char] = [pos for pos, c in enumerate(self.word) if c == char]
            else:
                self.remaining_guesses -= 1
        else:
            raise ValueError(self.get_status())

    def get_masked_word(self):
        for char, pos_list in self.char_pos_list.items():
            for pos in pos_list:
                temp = list(self.masked_word)
                temp[pos] = char
                self.masked_word = "".join(temp)
        return self.masked_word

    def get_status(self):
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        if "_" not in self.get_masked_word():
            self.status = STATUS_WIN
        return self.status
