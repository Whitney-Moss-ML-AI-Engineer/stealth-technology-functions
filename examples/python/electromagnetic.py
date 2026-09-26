"""Basic electromagnetic calculations."""
import cmath

def wavelength(frequency_hz, speed_m_s=299_792_458.0):
    if frequency_hz <= 0:
        raise ValueError("Frequency must be positive.")
    return speed_m_s / frequency_hz

def reflection_coefficient(z_load, z_medium):
    if z_load + z_medium == 0:
        raise ValueError("Invalid impedance combination.")
    return (z_load - z_medium) / (z_load + z_medium)

def reflection_power(coefficient):
    return abs(coefficient) ** 2

if __name__ == "__main__":
    f = 10e9
    lam = wavelength(f)
    gamma = reflection_coefficient(complex(75, 5), complex(50, 0))
    print(f"Wavelength: {lam * 1000:.3f} mm")
    print(f"Reflection coefficient: {gamma:.4f}")
    print(f"Reflected power fraction: {reflection_power(gamma):.4f}")
