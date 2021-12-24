class WedstrijdKansen:
    def __init__(self, thuis, uit, kansen):
        self.thuis = thuis
        self.uit = uit
        self.win = kansen[0]
        self.gelijk = kansen[1]
        self.verlies = kansen[2]