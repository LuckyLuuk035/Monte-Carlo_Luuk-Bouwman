from Middle_square import MidSquareGen


class Wedstrijd:
    def __init__(self, thuis, uit, kansen):
        self.thuis = thuis
        self.uit = uit
        self.win = kansen[0] / 100
        self.gelijk = (kansen[0] + kansen[1]) / 100

    def speelWedstrijd(self, seed):
        print(self.thuis.naam, self.uit.naam, self.win, self.gelijk, seed)
        if self.win >= seed:
            print(self.thuis.naam, "+3 punten")
            print(self.uit.naam, "0 punten")
        elif self.gelijk >= seed:
            print(self.thuis.naam, self.uit.naam, "beide +1 punten")

        elif seed < 1:
            print(self.thuis.naam, "0 punten")
            print(self.uit.naam, "+3 punten")
        else:
            raise IndexError
        print("")
