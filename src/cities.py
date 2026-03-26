import numpy as np

def generate_cities(n, size=300):
    return np.random.rand(n, 2) * size