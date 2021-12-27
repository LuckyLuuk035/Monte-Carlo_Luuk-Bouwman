import numpy as np
import pandas as pd

from Competitie import Competitie


class MonteCarloSimulatie:
    def __init__(self, seed):
        self.competitie = Competitie(seed)
        self.competitie.printStanding = False

        self.scoreboard = pd.DataFrame(np.zeros((5, 5)),
                                       columns=[team.naam for team in self.competitie.teams])
        self.scoreboard.index += 1

        self.voorspelling = self.scoreboard.copy()

    def runSimulatie(self, aantal):
        for i in range(aantal):
            resultaat = self.competitie.speelCompetitie()
            for j in resultaat:
                self.scoreboard[j][resultaat.get(j)] += 1
        print(self.scoreboard)

        self.updateVoorspelling(aantal)

    def updateVoorspelling(self, aantal):
        for kolom in self.scoreboard:
            for index, value in enumerate(self.scoreboard[kolom]):
                # print(kolom, index + 1, value)
                if value != 0:
                    self.voorspelling[kolom][index + 1] = (value / aantal) * 100
        print(self.voorspelling)
