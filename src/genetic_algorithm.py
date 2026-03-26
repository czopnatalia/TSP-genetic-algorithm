import random
from src.selection import get_selected_parent
from src.operators import crossover_ox, mutate_swap
from src.objective_function import calculate_distance

def run_genetic_algorithm(cities, selection_method, n_cities, pop_size, generations, p_mutation, p_crossover):
    population = [random.sample(range(n_cities), n_cities) for _ in range(pop_size)]
    history = []
    
    for gen in range(generations):
        fitnesses = [calculate_distance(ind, cities) for ind in population]
        best_idx = np.argmin(fitnesses)
        history.append(fitnesses[best_idx])
        
        new_pop = [population[best_idx]] # Elitaryzm
        while len(new_pop) < pop_size:
            p1 = get_selected_parent(population, fitnesses, method=selection_method)
            p2 = get_selected_parent(population, fitnesses, method=selection_method)
            
            child = crossover_ox(p1, p2) if random.random() < p_crossover else p1[:]
            if random.random() < p_mutation:
                child = mutate_swap(child)
            new_pop.append(child)
        population = new_pop
        
    return history