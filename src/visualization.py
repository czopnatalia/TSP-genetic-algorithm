import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


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


def animate_routes(cities, best_routes, interval=200):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        route = best_routes[frame]
        path = cities[route + [route[0]]]

        ax.plot(path[:, 0], path[:, 1], '-o')
        ax.set_title(f"Generation {frame}")

    anim = FuncAnimation(fig, update, frames=len(best_routes), interval=interval)
    plt.show()