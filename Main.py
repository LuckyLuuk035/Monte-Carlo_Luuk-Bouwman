from Middle_square import MidSquareGen
from Voetbal_club import VoetbalClub

rng = MidSquareGen(12345)

print([rng.next() for _ in range(20)])

# Neem tweemaal een random getal met steeds dezelfde seed
rng.reset(12345)
a = rng.next()
rng.reset(12345)
b = rng.next()

print(a)
print(a == b)  # Deze moeten gelijk zijn


Ajax = VoetbalClub("Ajax")
Feyenoord = VoetbalClub("Feyenoord")
PSV = VoetbalClub("PSV")
FC_Utrecht = VoetbalClub("FC Utrecht")
Willem_II = VoetbalClub("Willem II")
