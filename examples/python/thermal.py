"""Planck and Stefan-Boltzmann examples."""
import math

H = 6.62607015e-34
C = 299_792_458.0
K = 1.380649e-23
SIGMA = 5.670374419e-8

def planck_radiance(wavelength_m, temperature_k):
    if wavelength_m <= 0 or temperature_k <= 0:
        raise ValueError("Inputs must be positive.")
    numerator = 2 * H * C**2
    denominator = wavelength_m**5 * math.expm1(H * C / (wavelength_m * K * temperature_k))
    return numerator / denominator

def stefan_boltzmann_flux(temperature_k):
    if temperature_k < 0:
        raise ValueError("Temperature cannot be negative Kelvin.")
    return SIGMA * temperature_k**4

if __name__ == "__main__":
    print(f"Spectral radiance: {planck_radiance(10e-6, 300):.4e}")
    print(f"Radiative flux: {stefan_boltzmann_flux(300):.2f} W/m^2")
