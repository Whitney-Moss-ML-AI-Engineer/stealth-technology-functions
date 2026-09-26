"""Basic optical observability calculations."""

def contrast(object_signal, background_signal):
    if background_signal == 0:
        raise ValueError("Background cannot be zero.")
    return (object_signal - background_signal) / background_signal

def reflectance(reflected_energy, incident_energy):
    if incident_energy <= 0 or reflected_energy < 0:
        raise ValueError("Invalid energy values.")
    return reflected_energy / incident_energy

if __name__ == "__main__":
    print(f"Normalized contrast: {contrast(120, 100):.2f}")
    print(f"Reflectance: {reflectance(35, 100):.2f}")
