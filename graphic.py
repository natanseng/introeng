#Importando pacotes ( import (pacote) como a sigla (YYY) )


import numpy as np  
import matplotlib.pyplot as plt 
import soundfile as sf 

caminho = input("Insira o caminho do arquivo: ")

#Lendo amostra

signal, samplerate = sf.read(caminho)

#Definindo como será o gráfico

time = np.arange(0, len(signal) * 1/samplerate, 1/samplerate )

#Exibindo gráfico 
plt.plot(time,signal)
plt.show()
