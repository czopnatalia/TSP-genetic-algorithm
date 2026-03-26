import matplotlib.pyplot as plt

def plot_route(route, cities):
    path = cities[route + [route[0]]]
    plt.plot(path[:,0], path[:,1], '-o')
    plt.title("Best route")
    plt.show()


def plot_history(history):
    plt.plot(history)
    plt.title("Fitness over generations")
    plt.xlabel("Generation")
    plt.ylabel("Distance")
    plt.show()