import numpy as np

def generate_cities(n, area_size, on_circle=False):
    if on_circle:
        angles = np.linspace(0, 2*np.pi, n, endpoint=False)
        return np.stack([150 + 100*np.cos(angles), 150 + 100*np.sin(angles)], axis=1)
    return np.random.rand(n, 2) * area_size