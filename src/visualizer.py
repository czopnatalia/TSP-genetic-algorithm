import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import random
from src.selection import get_selected_parent
from src.operators import crossover_ox, mutate_swap
from src.objective_function import calculate_distance

def animation(cities, history, best_routes, area_size):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Przygotowanie wykresów
    line_best, = ax1.plot([], [], 'ro-', lw=2.5, markersize=6, label='Najlepszy')
    line_bg, = ax1.plot([], [], color='gray', alpha=0.2, lw=1, label='Populacja')
    ax1.set_xlim(-10, area_size + 10)
    ax1.set_ylim(-10, area_size + 10)
    ax1.set_title("Wizualizacja Trasy")
    ax1.legend()

    history_line, = ax2.plot([], [], 'b-', label='Najlepszy dystans')
    ax2.set_xlim(0, len(history))
    ax2.set_title("Postęp Optymalizacji")
    ax2.set_xlabel("Pokolenie")
    ax2.set_ylabel("Dystans")

    def update(frame):
        route = best_routes[frame]
        path = route + [route[0]]
        coords = cities[path]

        line_best.set_data(coords[:, 0], coords[:, 1])
        history_line.set_data(range(frame+1), history[:frame+1])

        ax2.set_ylim(min(history)*0.95, max(history)*1.05)

        return line_best, history_line

    ani = FuncAnimation(fig, update, frames=len(history), interval=50)
    return ani