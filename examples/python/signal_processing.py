"""FFT example using a synthetic signal."""
import numpy as np

def spectrum(signal, sample_rate_hz):
    n = len(signal)
    frequencies = np.fft.rfftfreq(n, d=1 / sample_rate_hz)
    amplitudes = np.abs(np.fft.rfft(signal)) / n
    return frequencies, amplitudes

if __name__ == "__main__":
    sample_rate = 1000
    t = np.arange(0, 1, 1 / sample_rate)
    signal = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
    frequencies, amplitudes = spectrum(signal, sample_rate)
    for f, a in zip(frequencies, amplitudes):
        if a > 0.1:
            print(f"{f:7.1f} Hz -> amplitude {a:.3f}")
