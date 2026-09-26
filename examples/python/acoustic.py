"""Basic acoustic calculations."""
import math

def sound_pressure_level(pressure_pa, reference_pressure_pa=20e-6):
    if pressure_pa <= 0 or reference_pressure_pa <= 0:
        raise ValueError("Pressures must be positive.")
    return 20 * math.log10(pressure_pa / reference_pressure_pa)

def pressure_from_spl(spl_db, reference_pressure_pa=20e-6):
    return reference_pressure_pa * 10 ** (spl_db / 20)

if __name__ == "__main__":
    print(f"SPL: {sound_pressure_level(0.002):.2f} dB")
    print(f"Pressure at 80 dB: {pressure_from_spl(80):.6f} Pa")
