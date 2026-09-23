import numpy as np
from scipy.io.wavfile import write

sr = 44100
duration = 4.8
t = np.arange(int(sr * duration)) / sr
audio = np.zeros_like(t)

def bell(freq, start, length, amp=0.5, decay=3.0):
    x = t - start
    mask = (x >= 0) & (x < length)
    xm = x[mask]
    env = (1 - np.exp(-xm * 90)) * np.exp(-xm * decay)
    sig = (np.sin(2*np.pi*freq*xm)
           + 0.48*np.sin(2*np.pi*freq*2.01*xm)
           + 0.22*np.sin(2*np.pi*freq*3.02*xm)
           + 0.10*np.sin(2*np.pi*freq*4.12*xm))
    y = np.zeros_like(t)
    y[mask] = amp * env * sig
    return y

melody = [
    (0.00,523.25,0.65,0.48), (0.38,659.25,0.65,0.50),
    (0.76,783.99,0.70,0.52), (1.14,1046.50,0.90,0.60),
    (1.72,987.77,0.55,0.42), (2.02,1046.50,0.55,0.48),
    (2.32,1174.66,0.65,0.52), (2.68,1318.51,1.35,0.62)
]
for start, freq, length, amp in melody:
    audio += bell(freq, start, length, amp)

for f, a in [(523.25,.30),(659.25,.30),(783.99,.30),(1046.50,.35),(1318.51,.22)]:
    audio += bell(f, 3.25, 1.45, a, decay=2.2)

for start, freq in [(3.45,1567.98),(3.65,2093.00),(3.88,2637.02)]:
    audio += bell(freq, start, 0.55, 0.13, decay=5.0)

audio /= max(np.max(np.abs(audio)), 1e-9)
audio *= 0.90
fade = int(0.35 * sr)
audio[-fade:] *= np.linspace(1, 0, fade)
write("finished.wav", sr, (audio * 32767).astype(np.int16))
