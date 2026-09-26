"""Simplified radar cross-section example. Educational model only."""
import math

def rcs_from_scattered_power(scattered_power, incident_power_density):
    """Simplified normalized RCS relationship."""
    if scattered_power < 0 or incident_power_density <= 0:
        raise ValueError("Invalid power values.")
    return 4 * math.pi * scattered_power / incident_power_density

if __name__ == "__main__":
    sigma = rcs_from_scattered_power(0.001, 1.0)
    print(f"Simplified normalized RCS: {sigma:.6f}")
