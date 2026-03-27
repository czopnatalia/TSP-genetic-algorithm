import random
import numpy as np
from src.selection import get_selected_parent
from src.operators import crossover_ox, mutate_swap
from src.objective_function import calculate_distance

def run_genetic_algorithm(cities, selection_method, n_cities, pop_size, generations, p_mutation, p_crossover):
    population = [random.sample(range(n_cities), n_cities) for _ in range(pop_size)]
    
    history = []
    best_routes = []

    best_overall_distance = float('inf')
    best_iteration = 0

    for gen in range(generations):
        fitnesses = [calculate_distance(ind, cities) for ind in population]
        best_idx = np.argmin(fitnesses)
        current_best = population[best_idx]
        current_best_dist = fitnesses[best_idx]

        history.append(current_best_dist)
        best_routes.append(current_best.copy())  

        # Sprawdzamy, czy znaleźliśmy nowy najlepszy wynik
        if current_best_dist < best_overall_distance:
            best_overall_distance = current_best_dist
            best_iteration = gen

        # Proces ewolucji
        new_pop = [current_best] # elitaryzm
        while len(new_pop) < pop_size:
            p1 = get_selected_parent(population, fitnesses, method=selection_method)
            p2 = get_selected_parent(population, fitnesses, method=selection_method)

            child = crossover_ox(p1, p2) if random.random() < p_crossover else p1[:]
            if random.random() < p_mutation:
                child = mutate_swap(child)

            new_pop.append(child)

        population = new_pop

    #print(f"\n--- KONIEC SYMULACJI ---")
    print(f"Metoda selekcji: {selection_method}")
    print(f"Minimalna droga: {best_overall_distance:.2f}")
    print(f"Osiągnięto ją w iteracji nr: {best_iteration}\n")

    return {
    "history": history,
    "best_overall_distance": best_overall_distance,
    "best_iteration": best_iteration,
    "best_routes": best_routes
    }