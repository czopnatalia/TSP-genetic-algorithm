import random

def crossover_ox(parent1, parent2):
    # Order Crossover (OX) - zachowuje permutację
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    
    child = [None] * size
    child[start:end] = parent1[start:end]
    
    # Uzupełnianie pozostałych z drugiego rodzica
    p2_remaining = [item for item in parent2 if item not in child]
    cursor = 0
    for i in range(size):
        if child[i] is None:
            child[i] = p2_remaining[cursor]
            cursor += 1
    return child

def mutate_swap(individual):
    # Zamiana dwóch losowych miast
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual