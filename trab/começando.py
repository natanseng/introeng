import numpy as np  
import matplotlib.pyplot as plt 
import soundfile as sf 

signal, samplerate = sf.read('audio.wav')

time = np.arange(0, len(signal) * 1/samplerate, 1/samplerate )

plt.plot(time,signal)
plt.show()
