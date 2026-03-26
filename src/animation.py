import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import random
from src.selection import get_selected_parent
from src.operators import crossover_ox, mutate_swap
from src.objective_function import calculate_distance

def run_genetic_animation(cities, selection_method, n_cities, pop_size, generations, p_mutation, p_crossover, area_size):
    # 1. PRZYGOTOWANIE FIGURY (Lokalnie wewnątrz funkcji)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    line_bg1, = ax1.plot([], [], color='gray', alpha=0.3, lw=1, label='10-ty osobnik')
    line_bg2, = ax1.plot([], [], color='silver', alpha=0.2, lw=0.8, label='30-ty osobnik')
    line_best, = ax1.plot([], [], 'ro-', lw=2.5, markersize=6, label='Najlepszy')
    
    ax1.set_xlim(-10, area_size + 10)
    ax1.set_ylim(-10, area_size + 10)
    ax1.legend(loc='upper right')
    best_text = ax1.set_title('')
    
    history_line, = ax2.plot([], [], 'b-')
    ax2.set_xlim(0, generations)
    ax2.set_title("Postęp optymalizacji")
    ax2.set_xlabel("Pokolenie")
    ax2.set_ylabel("Dystans")

    # 2. INICJALIZACJA POPULACJI
    # Używamy zmiennej lokalnej 'state', aby przechowywać populację między klatkami
    state = {
        'population': [random.sample(range(n_cities), n_cities) for _ in range(pop_size)],
        'history_dist': []
    }

    # 3. WEWNĘTRZNA FUNKCJA AKTUALIZUJĄCA
    def update(frame, state, cities, selection_method, p_mutation, p_crossover):
        pop = state['population']
        
        # Obliczanie przystosowania
        fitnesses = [calculate_distance(ind, cities) for ind in pop]
        ranked_indices = np.argsort(fitnesses)
        
        best_idx = ranked_indices[0]
        bg1_idx = ranked_indices[9] if len(ranked_indices) > 9 else best_idx
        bg2_idx = ranked_indices[29] if len(ranked_indices) > 29 else best_idx
        
        current_best_dist = fitnesses[best_idx]
        state['history_dist'].append(current_best_dist)
        
        # Aktualizacja wizualizacji trasy
        best_path = pop[best_idx] + [pop[best_idx][0]]
        coords_best = cities[best_path]
        line_best.set_data(coords_best[:, 0], coords_best[:, 1])
        
        line_bg1.set_data(cities[pop[bg1_idx] + [pop[bg1_idx][0]]][:, 0], 
                          cities[pop[bg1_idx] + [pop[bg1_idx][0]]][:, 1])
        line_bg2.set_data(cities[pop[bg2_idx] + [pop[bg2_idx][0]]][:, 0], 
                          cities[pop[bg2_idx] + [pop[bg2_idx][0]]][:, 1])
        
        best_text.set_text(f"Pokolenie: {frame} | Metoda: {selection_method} | Dystans: {current_best_dist:.2f}")
        
        # Aktualizacja wykresu postępu
        history_line.set_data(range(len(state['history_dist'])), state['history_dist'])
        ax2.set_ylim(min(state['history_dist'])*0.95, max(state['history_dist'])*1.05)
        
        # EWOLUCJA - Tworzenie nowej populacji
        new_pop = [pop[best_idx]] # Elitaryzm
        while len(new_pop) < pop_size:
            p1 = get_selected_parent(pop, fitnesses, method=selection_method)
            p2 = get_selected_parent(pop, fitnesses, method=selection_method)
            
            child = crossover_ox(p1, p2) if random.random() < p_crossover else p1[:]
            if random.random() < p_mutation:
                child = mutate_swap(child)
            new_pop.append(child)
        
        state['population'] = new_pop
        return line_best, line_bg1, line_bg2, history_line

    # 4. GENEROWANIE ANIMACJI
    # Przekazujemy parametry przez fargs
    ani = FuncAnimation(fig, update, frames=generations, 
                        fargs=(state, cities, selection_method, p_mutation, p_crossover),
                        interval=100, blit=True, repeat=False)
    
    plt.close() # Zamyka statyczne okno, wyświetli się tylko animacja HTML
    return ani