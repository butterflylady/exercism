class PhoneNumber:
    def __init__(self, number):
        self.number=number
        self.output_number=""

    def number(self):
        for s in self.number:
            if s in range(2,10):
                self.output_number+=s
                break

