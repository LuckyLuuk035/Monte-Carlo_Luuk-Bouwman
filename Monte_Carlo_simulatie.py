import numpy as np
import pandas as pd

from Competitie import Competitie


class MonteCarloSimulatie:
    """
    MonteCarloSimulatie is een simulatie model dat de winnaar van de competitie voorspeld.
    Dit doet het door gebruikt te maken van een Random Number Generator.
    """
    def __init__(self, seed):
        """
        :param seed: de start waarde die aan de Random Number Generator wordt meegegeven.

        Bij het aanmaken van een nieuwe simulatie wordt eerst de competie opgezet.
        Waarna het scoreboard van eind scores en een dataframe voor de voorspellingen wordt aagemaakt.
        """
        self.competitie = Competitie(seed)
        self.competitie.printStanding = False

        self.aantal = 0

        self.scoreboard = pd.DataFrame(np.zeros((5, 5)),
                                       columns=[team.naam for team in self.competitie.teams])
        self.scoreboard.index += 1
        self.voorspelling = self.scoreboard.copy()

    def runSimulatie(self, aantal):
        """
        runSimulatie runt de competie opnieuw tot het gevraagde aantal is behaald.

        :param aantal: het meegegeven aantal wat bepaald hoe vaak de competie wordt gerund.
        :return: een geupdate lijst met de percentages van de kans voor het behalen van elke positie.
        """
        self.aantal += aantal
        for i in range(aantal):
            resultaat = self.competitie.speelCompetitie()  # speel de competie.
            for j in resultaat:
                self.scoreboard[j][resultaat.get(j)] += 1  # pas het scoreboard aan.
        return self.updateVoorspelling()

    def updateVoorspelling(self):
        """
        updateVoorspelling past de dataframe van voorspellingen aan en vult hier het correcte percentage kans in.
        :return: de nieuwe lijst van voorspellingen.
        """
        for kolom in self.scoreboard:
            for index, value in enumerate(self.scoreboard[kolom]):
                if value != 0:  # het is niet mogelijk door 0 te delen.
                    self.voorspelling[kolom][index + 1] = (value / self.aantal) * 100
        return self.voorspelling
