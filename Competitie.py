from Middle_square import MidSquareGen

from Voetbal_club import VoetbalClub
from Wedstrijd import Wedstrijd

class Competitie:
    def __init__(self, seed):
        self.rng = MidSquareGen(seed)

        self.Ajax = VoetbalClub("Ajax")
        self.Feyenoord = VoetbalClub("Feyenoord")
        self.PSV = VoetbalClub("PSV")
        self.FC_Utrecht = VoetbalClub("FC Utrecht")
        self.Willem_II = VoetbalClub("Willem II")
        self.teams = [self.Ajax, self.Feyenoord, self.PSV, self.FC_Utrecht, self.Willem_II]

        self.wedstrijden = self.setupWedstrijden()

    def setupWedstrijden(self):
        w00 = Wedstrijd(self.Ajax, self.Feyenoord, [65, 17, 18])
        w01 = Wedstrijd(self.Ajax, self.PSV, [54, 21, 25])
        w02 = Wedstrijd(self.Ajax, self.FC_Utrecht, [74, 14, 12])
        w03 = Wedstrijd(self.Ajax, self.FC_Utrecht, [78, 13, 9])

        w10 = Wedstrijd(self.Feyenoord, self.Ajax, [30, 21, 49])
        w11 = Wedstrijd(self.Feyenoord, self.PSV, [37, 24, 39])
        w12 = Wedstrijd(self.Feyenoord, self.FC_Utrecht, [51, 22, 27])
        w13 = Wedstrijd(self.Feyenoord, self.PSV, [60, 21, 19])

        w20 = Wedstrijd(self.PSV, self.Ajax, [39, 22, 39])
        w21 = Wedstrijd(self.PSV, self.Feyenoord, [54, 22, 24])
        w22 = Wedstrijd(self.PSV, self.FC_Utrecht, [62, 20, 18])
        w23 = Wedstrijd(self.PSV, self.Willem_II, [62, 22, 16])

        w30 = Wedstrijd(self.FC_Utrecht, self.Ajax, [25, 14, 61])
        w31 = Wedstrijd(self.FC_Utrecht, self.Feyenoord, [37, 23, 40])
        w32 = Wedstrijd(self.FC_Utrecht, self.PSV, [29, 24, 47])
        w33 = Wedstrijd(self.FC_Utrecht, self.Willem_II, [52, 23, 25])

        w40 = Wedstrijd(self.Willem_II, self.Ajax, [17, 18, 65])
        w41 = Wedstrijd(self.Willem_II, self.Feyenoord, [20, 26, 54])
        w42 = Wedstrijd(self.Willem_II, self.PSV, [23, 24, 53])
        w43 = Wedstrijd(self.Willem_II, self.FC_Utrecht, [37, 25, 38])
        return [w00, w01, w02, w03,
                w10, w11, w12, w13,
                w20, w21, w22, w23,
                w30, w31, w32, w33,
                w40, w41, w42, w43]

    def speelCompetitie(self):
        for wedstrijd in self.wedstrijden:
            random = self.rng.next()
            wedstrijd.speelWedstrijd(random)
        self.berekenUitkomst()

    def berekenUitkomst(self):
        uitkomst = [[self.Ajax]]
        for team in self.teams:
            for index, plaats in enumerate(uitkomst):
                if team.punten > plaats[0].punten:
                    uitkomst = uitkomst[0:index-1] + [team] + uitkomst[index-1:]
                    break
                elif team.punten == plaats[0].punten:
                    # alleen voor Ajax en check tegen duplicates.
                    if team == plaats[0]:
                        break
                    plaats.append(team)
                    break
                elif uitkomst[-1] == plaats:
                    uitkomst.append([team])
                    break
            self.printUitkomst(uitkomst)

    def printUitkomst(self, uitkomst):
        plaats = 1
        for teams in uitkomst:
            if len(teams) != 1:
                for team in teams:
                    print("In " + str(plaats) + "e plaats: " + team.naam + " met " + str(team.punten) + " punten")
                plaats += len(teams)
            else:
                print("In " + str(plaats) + "e plaats: " + teams[0].naam + " met " + str(teams[0].punten) + " punten")
                plaats += 1
        print("")
