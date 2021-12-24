from Middle_square import MidSquareGen

from Voetbal_club import VoetbalClub
from Wedstrijd import Wedstrijd

class Competitie:
    def __init__(self, rng):
        self.Ajax = VoetbalClub("Ajax")
        self.Feyenoord = VoetbalClub("Feyenoord")
        self.PSV = VoetbalClub("PSV")
        self.FC_Utrecht = VoetbalClub("FC Utrecht")
        self.Willem_II = VoetbalClub("Willem II")

    def setupWedstrijden(self):
        w00 = Wedstrijd(self.Ajax, self.Feyenoord, [65, 17, 18])
        w01 = Wedstrijd(self.Ajax, self.PSV, [54, 21, 25])
        w02 = Wedstrijd(self.Ajax, self.FC_Utrecht, [74, 14, 12])
        w02 = Wedstrijd(self.Ajax, self.FC_Utrecht, [78, 13, 9])

        w10 = Wedstrijd(self.Feyenoord, self.Ajax, [30, 21, 49])
        w11 = Wedstrijd(self.Feyenoord, self.PSV, [37, 24, 39])
        w12 = Wedstrijd(self.Feyenoord, self.FC_Utrecht, [51, 22, 27])
        w13 = Wedstrijd(self.Feyenoord, self.PSV, [60, 21, 19])

        w20 = Wedstrijd(self.PSV, self.Ajax, [39, 22, 39])
        w21 = Wedstrijd(self.PSV, self.Feyenoord, [54, 22, 24])
        w22 = Wedstrijd(self.PSV, self.FC_Utrecht, [62, 20, 18])
        w23 = Wedstrijd(self.PSV, self.Willem_II, [62, 22, 16])

        w20 = Wedstrijd(self.FC_Utrecht, self.Ajax, [25, 14, 61])
        w21 = Wedstrijd(self.FC_Utrecht, self.Feyenoord, [37, 23, 40])
        w22 = Wedstrijd(self.FC_Utrecht, self.PSV, [29, 24, 47])
        w23 = Wedstrijd(self.FC_Utrecht, self.Willem_II, [52, 23, 25])

        w20 = Wedstrijd(self.Willem_II, self.Ajax, [17, 18, 65])
        w21 = Wedstrijd(self.Willem_II, self.Feyenoord, [20, 26, 54])
        w22 = Wedstrijd(self.Willem_II, self.PSV, [23, 24, 53])
        w23 = Wedstrijd(self.Willem_II, self.FC_Utrecht, [37, 25, 38])

