class Wedstrijd:
    def __init__(self, thuis, uit, kansen):
        self.thuis = thuis
        self.uit = uit
        self.win = kansen[0] / 100
        self.gelijk = (kansen[0] + kansen[1]) / 100

    def speelWedstrijd(self, seed):
        # print(self.thuis.naam, self.uit.naam, self.win, self.gelijk, seed)
        if self.win >= seed:
            self.thuis.punten += 3
            # print(self.thuis.naam, "+3 punten. Totaal:", self.thuis.punten)
            # print(self.uit.naam, "0 punten. Totaal:", self.uit.punten)

        elif self.gelijk >= seed:
            self.thuis.punten += 1
            self.uit.punten += 1
            # print(self.thuis.naam, "+1 punt. Totaal:", self.thuis.punten)
            # print(self.uit.naam, "+1 punt. Totaal:", self.uit.punten)


        elif seed < 1:
            self.uit.punten += 3
            # print(self.thuis.naam, "0 punten. Totaal:", self.thuis.punten)
            # print(self.uit.naam, "+3 punten. Totaal:", self.uit.punten)
        else:
            raise IndexError
