from Middle_square import MidSquareGen


class Wedstrijd:
    def __init__(self, thuis, uit, kansen):
        self.thuis = thuis
        self.uit = uit
        self.win = kansen[0]
        self.gelijk = kansen[1]
        self.verlies = kansen[2]

    def speelWedstrijd(self, seed):
        print(self.thuis, self.uit, seed)
