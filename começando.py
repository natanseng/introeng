#Importando pacotes ( import (pacote) como a sigla (YYY) )


import numpy as np  
import matplotlib.pyplot as plt 
import soundfile as sf 

#Lendo amostra

signal, samplerate = sf.read('audio.wav')

#Definindo como será o gráfico

time = np.arange(0, len(signal) * 1/samplerate, 1/samplerate )

#Exibindo gráfico 
plt.plot(time,signal)
plt.show()
