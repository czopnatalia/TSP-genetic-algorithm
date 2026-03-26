import numpy as np
import random

def get_selected_parent(population, fitnesses, method="ranking"):
    if method == "roulette":
        # # Ruletka: szansa proporcjonalna do 1/dystans (im mniejszy dystans, tym większa szansa)
        inverted_fitness = 1.0 / np.array(fitnesses)
        probs = inverted_fitness / inverted_fitness.sum()
        idx = np.random.choice(len(population), p=probs)
        return population[idx]

    elif method == "ranking":
        # Sortujemy indeksy populacji od najlepszego (najkrótszy dystans) do najgorszego
        ranked_indices = np.argsort(fitnesses)
        # Prawdopodobieństwo liniowe: najlepszy ma największą szansę
        n = len(population)
        probs = np.linspace(2, 0, n) / n  # Prosta metoda rankingowa
        # Przypisujemy prawdopodobieństwa do posortowanych osobników
        selected_idx = np.random.choice(ranked_indices, p=probs)
        return population[selected_idx]

    elif method == "tournament":
        # Turniejowa: losujemy 3 osobników, wygrywa najlepszy
        candidates_idx = random.sample(range(len(population)), 3)
        best_candidate_idx = candidates_idx[np.argmin([fitnesses[i] for i in candidates_idx])]
        return population[best_candidate_idx]