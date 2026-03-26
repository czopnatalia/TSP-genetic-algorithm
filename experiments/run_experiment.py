import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import config
from src.cities import generate_cities
from src.genetic_algorithm import run_genetic_algorithm
from src.visualization import plot_route, plot_history, animate_routes

cities = generate_cities(config.N_CITIES, config.AREA_SIZE, on_circle=False)

population, history, best_routes = run_genetic_algorithm(cities, config)

best = min(population, key=lambda x: sum(history))

# plot_route(best, cities)
# plot_history(history)
animate_routes(cities, best_routes)