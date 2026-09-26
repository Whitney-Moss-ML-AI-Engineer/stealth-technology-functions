"""Monte Carlo uncertainty-propagation example."""
import numpy as np

def simulate(n=100_000, seed=42):
    rng = np.random.default_rng(seed)
    frequency = rng.normal(10e9, 0.1e9, n)
    speed = rng.normal(299_792_458.0, 100.0, n)
    wavelength = speed / frequency
    return {
        "mean_m": np.mean(wavelength),
        "std_m": np.std(wavelength),
        "p05_m": np.percentile(wavelength, 5),
        "p95_m": np.percentile(wavelength, 95),
    }

if __name__ == "__main__":
    for key, value in simulate().items():
        print(f"{key}: {value:.6e}")
