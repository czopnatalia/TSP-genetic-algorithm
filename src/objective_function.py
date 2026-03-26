import numpy as np

def total_distance(route, cities):
    dist = 0
    for i in range(len(route)):
        a = cities[route[i]]
        b = cities[route[(i+1) % len(route)]]
        dist += np.linalg.norm(a - b)
    return dist