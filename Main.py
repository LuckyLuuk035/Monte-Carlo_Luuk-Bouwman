from Middle_square import MidSquareGen

from Monte_Carlo_simulatie import MonteCarloSimulatie

seed = 12345

simulatie = MonteCarloSimulatie(seed)

print(simulatie.runSimulatie(2000))