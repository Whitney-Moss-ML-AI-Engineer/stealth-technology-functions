"""Generic exponential attenuation demonstration."""
import math

def transmitted_intensity(initial_intensity, attenuation_coefficient, thickness_m):
    if initial_intensity < 0 or attenuation_coefficient < 0 or thickness_m < 0:
        raise ValueError("Values must be nonnegative.")
    return initial_intensity * math.exp(-attenuation_coefficient * thickness_m)

if __name__ == "__main__":
    transmitted = transmitted_intensity(1.0, 12.0, 0.05)
    print(f"Transmitted fraction: {transmitted:.4f}")
    print(f"Absorbed fraction: {1 - transmitted:.4f}")
