import random
from src.selection import roulette, ranking
from src.operators import crossover, mutate
from src.objective_function import total_distance

def run_ga(cities, config):
    population = [random.sample(range(len(cities)), len(cities)) 
                  for _ in range(config.POP_SIZE)]

    history = []

    for gen in range(config.GENERATIONS):
        fitnesses = [total_distance(ind, cities) for ind in population]

        new_pop = []

        for _ in range(config.POP_SIZE):
            if config.SELECTION_METHOD == "roulette":
                select = roulette
            else:
                select = ranking

            p1 = select(population, fitnesses)
            p2 = select(population, fitnesses)

            child = crossover(p1, p2) if random.random() < config.CROSSOVER_PROB else p1[:]
            child = mutate(child, config.MUTATION_PROB)

            new_pop.append(child)

        population = new_pop
        history.append(min(fitnesses))

    return population, history