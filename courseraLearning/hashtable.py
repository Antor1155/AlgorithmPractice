class Calc():
    def __init__(self, number=0):
        self.number = number
        self.x = None

    def add(self, value):
        self.number = self.number + value
        self.x = self

    def subtract(self, value):
        self.number = self.number - value
        return self


calc = Calc()

k = calc.add(5)
print(calc.x)  # 👉️ 8


