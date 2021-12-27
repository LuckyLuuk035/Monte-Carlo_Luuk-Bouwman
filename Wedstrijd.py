class Wedstrijd:
    """
    Wedstrijd is een simpele class.
    """
    def __init__(self, thuis, uit, kansen):
        """
        :param thuis: het thuis spelende team.
        :param uit: het uit spelende team.
        :param kansen: een lijst van kansen op winnen, gelijkspelen of verliezen.
        """
        self.thuis = thuis
        self.uit = uit
        self.win = kansen[0] / 100
        self.gelijk = (kansen[0] + kansen[1]) / 100

    def speelWedstrijd(self, seed):
        """
        speelWedstrijd "speelt" de wedstrijden en geeft de teams het aantal punten.
        :param seed: de seed is een 0-1 getal en bepaald welke partij wint.
        """
        if self.win >= seed:
            self.thuis.punten += 3

        elif self.gelijk >= seed:
            self.thuis.punten += 1
            self.uit.punten += 1

        elif seed < 1:
            self.uit.punten += 3
        else:
            raise IndexError
