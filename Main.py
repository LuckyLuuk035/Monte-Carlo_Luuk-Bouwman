from Middle_square import MidSquareGen

rng = MidSquareGen(12345)

print([rng.next() for _ in range(20)])

# Neem tweemaal een random getal met steeds dezelfde seed
rng.reset(12345)
a = rng.next()
rng.reset(12345)
b = rng.next()
print(a == b)  # Deze moeten gelijk zijn