import numpy as np
import pandas as pd

from Competitie import Competitie


class MonteCarloSimulatie:
    def __init__(self, seed):
        self.competitie = Competitie(seed)
        self.competitie.printStanding = True
        self.competitie_scoreboard = pd.DataFrame(np.zeros((5, 5)), columns=[team.naam for team in self.competitie.teams])
        self.competitie_scoreboard.index += 1

    def runSimulatie(self, aantal):
        for i in range(aantal):
            resultaat = self.competitie.speelCompetitie()
            for j in resultaat:
                self.competitie_scoreboard[j][resultaat.get(j)] += 1
                print(self.competitie_scoreboard)
