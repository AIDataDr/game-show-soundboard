import numpy as np
from scipy.io.wavfile import write

sr = 44100
duration = 1.7
t = np.arange(int(sr * duration)) / sr
audio = np.zeros_like(t)

def bell(freq, start, length, amp):
    x = t - start
    mask = (x >= 0) & (x < length)
    y = np.zeros_like(t)
    xm = x[mask]
    env = (1 - np.exp(-xm * 80)) * np.exp(-xm * 4.5)
    sig = (np.sin(2*np.pi*freq*xm)
           + 0.55*np.sin(2*np.pi*freq*2.01*xm)
           + 0.28*np.sin(2*np.pi*freq*3.03*xm)
           + 0.14*np.sin(2*np.pi*freq*4.15*xm))
    y[mask] = amp * env * sig
    return y

for start, freq, length, amp in [
    (0.00, 659.25, 0.45, 0.65),
    (0.28, 783.99, 0.45, 0.70),
    (0.56, 1046.50, 0.85, 0.80),
]:
    audio += bell(freq, start, length, amp)

for f in [523.25, 659.25, 783.99, 1046.50]:
    audio += bell(f, 0.82, 0.75, 0.24)

audio /= max(np.max(np.abs(audio)), 1e-9)
audio *= 0.92
fade_len = int(0.18 * sr)
audio[-fade_len:] *= np.linspace(1, 0, fade_len)
write("correct_winner.wav", sr, (audio * 32767).astype(np.int16))
