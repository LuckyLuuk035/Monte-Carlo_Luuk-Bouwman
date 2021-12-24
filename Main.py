from Middle_square import MidSquareGen

from Competitie import Competitie

seed = 12345
rng = MidSquareGen(seed)

print([rng.next() for _ in range(20)])

# Neem tweemaal een random getal met steeds dezelfde seed
rng.reset(12345)

# -----------------------------------------------------------

c = Competitie(seed)

c.speelCompetitie()