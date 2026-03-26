from src import config
from src.cities import generate_cities
from src.genetic_algorithm import run_ga
from src.visualization import plot_route, plot_history

cities = generate_cities(config.N_CITIES)

population, history = run_ga(cities, config)

best = min(population, key=lambda x: sum(history))

plot_route(best, cities)
plot_history(history)