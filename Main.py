from Monte_Carlo_simulatie import MonteCarloSimulatie

seed = 123456789

# Ga naar 'competie' om de RNG aan te passen.

simulatie = MonteCarloSimulatie(seed)
print(simulatie.runSimulatie(5000))
