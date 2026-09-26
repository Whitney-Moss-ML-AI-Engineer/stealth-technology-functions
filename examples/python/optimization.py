"""Simple objective-function and grid-search example."""
import numpy as np

def objective(x):
    return (x - 3.0)**2 + 2.0

def grid_search(lower, upper, step):
    values = np.arange(lower, upper + step, step)
    scores = np.array([objective(x) for x in values])
    index = np.argmin(scores)
    return values[index], scores[index]

if __name__ == "__main__":
    x, score = grid_search(-10, 10, 0.01)
    print(f"Best grid point: {x:.2f}")
    print(f"Objective value: {score:.4f}")
