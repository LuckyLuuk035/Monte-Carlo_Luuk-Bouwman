class LinearCongruentialGenerator:
    def __init__(self, seed):
        self.state = seed
        self.multiply = 424731
        self.add = 23

    def next(self):
        self.state = self.LinearCongruential(self.state)
        # Dit "random" nummer deel je door 100000 en geef je terug.
        return self.state / 100000

    def LinearCongruential(self, number):
        """
        Neem de imput en vermenig vuldig deze met het bepaalde getal.
        Voel dan het add getal toe, waarna je de laatste 5 getallen pakt.
        """
        number = number * self.multiply
        number += self.add
        number = int(str(number)[-5:])
        return number
