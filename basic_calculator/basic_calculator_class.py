

class BasicCalculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return  self.x * self.y

    def devide(self):
        return self.x / self.y


myCalc = BasicCalculator(15, 56)
mySum = myCalc.add()
print(mySum)