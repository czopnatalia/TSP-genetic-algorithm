import numpy as np

def calculate_distance(path, cities):
    # Suma odległości euklidesowych
    dist = 0
    for i in range(len(path)):
        city_a = cities[path[i]]
        city_b = cities[path[(i + 1) % len(path)]] # Powrót do początku
        dist += np.linalg.norm(city_a - city_b)
    return dist