class MidSquareGen(object):  # Algemene opzet voor een RNG object: init, en next. Optioneel (re)set seed.
    def __init__(self, seed):
        self.seed = seed

    def reset(self, seed):
        self.seed = seed

    def next(self):
        self.seed = MidSquareGen.select_middle(self.seed ** 2, 4)  # Bereken volgende seed (en bewaar die)
        return self.seed / 10000.0  # Bereken waarde uit seed (kan de geschaalde seed zijn, of een complexere functie)

    @staticmethod
    def select_middle(number, positions):  # Statische helperfunctie
        left = True
        while len(str(number)) > positions:
            if left:
                number = int(str(number)[1:])
                left = False
            else:
                number = int(str(number)[:-1])
                left = True
        return number


