import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import config
from IPython.display import HTML
import matplotlib.pyplot as plt

from src.cities import generate_cities
from src.logic import run_genetic_algorithm
from src.visualizer import animation

N_CITIES = 20          # Liczba miast
POP_SIZE = 100         # Wielkość populacji
P_CROSSOVER = 0.9      # Prawdopodobieństwo krzyżowania
P_MUTATION = 0.08      # Prawdopodobieństwo mutacji
GENERATIONS = 200      # Liczba pokoleń
AREA_SIZE = 300        # Obszar 300x300

cities=generate_cities(N_CITIES, AREA_SIZE, on_circle=False)
cities_circle=generate_cities(N_CITIES, AREA_SIZE, on_circle=True)

# Porównanie metod selekcji
methods = ["roulette", "ranking", "tournament"]
results_data = {}

print("---Uruchamianie symulacji porównawczej---\n")

for m in methods:
    res = run_genetic_algorithm(cities, m, N_CITIES, POP_SIZE, GENERATIONS, P_MUTATION, P_CROSSOVER)
    results_data[m] = res
    
    # Wypisujemy krótkie podsumowanie w konsoli
    #print(f"  -> Najlepszy dystans: {res['best_overall_distance']:.2f}")
    #print(f"  -> Znaleziono w pokoleniu: {res['best_iteration']}")

# Wizualizacja porównawcza
plt.figure(figsize=(12, 7))

for m, res in results_data.items():
    # Pobieramy listę historii ze słownika
    plt.plot(res['history'], label=f"Selekcja: {m} (Best distance: {res['best_overall_distance']:.2f})")

plt.title("Porównanie metod selekcji w problemie Komiwojażera")
plt.xlabel("Pokolenie")
plt.ylabel("Najlepszy dystans")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Dodatkowa optymalizacja: dodanie punktu w miejscu znalezienia minimum dla każdej metody
for m, res in results_data.items():
    plt.scatter(res['best_iteration'], res['best_overall_distance'], s=50)

# Zapis do pliku
output_path = './results/plots/selection_method_comparision.png'
directory = os.path.dirname(output_path)
plt.savefig(output_path)

plt.show()

