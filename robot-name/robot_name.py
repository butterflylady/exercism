import random
import string

name_set = set()


class Robot:
    def __init__(self):
        self.name = self._generate_name()

    def _generate_name(self):
        name = "".join(random.choices(string.ascii_uppercase, k=2)) + "".join(random.choices(string.digits, k=3))
        if name in name_set:
            self._generate_name()
        return name

    def reset(self):
        self.name = self._generate_name()
