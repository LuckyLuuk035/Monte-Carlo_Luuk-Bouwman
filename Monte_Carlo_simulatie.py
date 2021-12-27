from Middle_square import MidSquareGen
from Competitie import Competitie


class MonteCarloSimulatie:
    def __init__(self, seed):
        self.competitie = Competitie(seed)
        self.competitie.printStanding = True
        self.results = {}

    def runSimulatie(self, aantal):
        for i in range(aantal):
            resultaat = self.competitie.speelCompetitie()
            print(resultaat)