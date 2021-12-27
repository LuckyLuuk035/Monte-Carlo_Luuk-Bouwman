from Monte_Carlo_simulatie import MonteCarloSimulatie
from Linear_congruential_generator import LinearCongruentialGenerator

seed = 123456789


rng = LinearCongruentialGenerator(seed)
[print(rng.next()) for i in range(30)]

# simulatie = MonteCarloSimulatie(seed)
# print(simulatie.runSimulatie(2000))
