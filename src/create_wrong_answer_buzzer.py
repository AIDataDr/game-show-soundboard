import numpy as np
from scipy.io.wavfile import write

sr = 44100
duration = 1.25
t = np.arange(int(sr * duration)) / sr
audio = np.zeros_like(t)

def buzzer(freq, start, length, amp=1.0):
    x = t - start
    mask = (x >= 0) & (x < length)
    xm = x[mask]
    env = np.minimum(1.0, xm / 0.008) * np.minimum(1.0, (length - xm) / 0.04)
    sig = (0.70*np.sign(np.sin(2*np.pi*freq*xm))
           + 0.20*np.sin(2*np.pi*(freq*1.5)*xm)
           + 0.10*np.sin(2*np.pi*(freq*0.99)*xm))
    y = np.zeros_like(t)
    y[mask] = amp * env * sig
    return y

audio += buzzer(185, 0.00, 0.48, 0.8)
audio += buzzer(138, 0.52, 0.62, 0.9)
audio /= max(np.max(np.abs(audio)), 1e-9)
audio *= 0.88
write("wrong_answer_buzzer.wav", sr, (audio * 32767).astype(np.int16))
