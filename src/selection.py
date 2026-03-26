import numpy as np

def roulette(population, fitnesses):
    probs = [1/f for f in fitnesses]
    probs = np.array(probs) / sum(probs)
    return population[np.random.choice(len(population), p=probs)]


def ranking(population, fitnesses):
    ranked = sorted(zip(population, fitnesses), key=lambda x: x[1])
    probs = np.linspace(1, 0, len(population))
    probs /= probs.sum()
    return ranked[np.random.choice(len(population), p=probs)][0]