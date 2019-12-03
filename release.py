# Introdução à Engenharia de Computação - Profº Antônio - UFBA - 2019.2 #
# Trabalho realizado por Natan Santos e Pedro Viana. #

# Elaborado utilizando o Git e integrado com o GitHub, plataforma online de versionamento e compartilhamento de códigos. #

import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
import os
from pydub import AudioSegment
import wave
from tkinter.filedialog import askdirectory


musicas_mp3 = list()
musicas_wav = list()

# Buscando Áudio

def busca_wav():
    print('Qual diretório deseja buscar os arquivos .WAV? ')
    diretorio_raiz = askdirectory()
    for file in os.listdir(diretorio_raiz):
        if file.endswith(".wav"):
            musicas_wav.append(str(file))
        elif file.endswith(".mp3"):
            musicas_mp3.append(str(file))
    return diretorio_raiz

# Converter para .wav

def converte_para_wav():
    for musica in musicas_mp3:
        sound = AudioSegment.from_mp3(diretorio_raiz + "/" + musica)
        sound.export((diretorio_raiz + "/" + musica).replace('.mp3', '.wav'), format="wav")
        musicas_wav.append(musica.replace('.mp3', '.wav'))
        os.remove(diretorio_raiz + "/" + musica)
        
def renomeia_wav():
    cont = 1
    for musica in musicas_wav:
        os.rename(diretorio_raiz + "/" + recupera_nome_musica(musica), diretorio_raiz + "/" + str(cont)+".wav")
        cont = cont + 1

#Pegando nome da Música

def recupera_nome_musica(musica):
    partes = musica.split('\\')
    return partes[len(partes) - 1]

# Stereo to mono

def downmixing():
  	for musica in musicas_wav:
          arquivo_carregado = wave.open(diretorio_raiz + "/" + musica, 'r')
          if arquivo_carregado.getnchannels() != 1:
              arquivo_mono = AudioSegment.from_wav(diretorio_raiz + "/" + musica, 'r')
              arquivo_mono = arquivo_mono.set_channels(1)
              arquivo_mono.export(diretorio_raiz + "/" + musica, format="wav")

# Gráfico

def plota_grafico():
    i = input("Escolha o número da música que você quer: ")
    caminho = diretorio_raiz + "/" + str(i) + ".wav"

    #Lendo amostra

    signal, samplerate = sf.read(caminho)

    #Definindo como será o gráfico

    time = np.arange(0, len(signal) * 1/samplerate, 1/samplerate )

    #Exibindo gráfico 
    plt.title("Gráfico do arquivo " + str(i) + ".wav:")
    plt.plot(time,signal)
    plt.show()

# Feature

def learn_audio():
    # Definindo input do arquivo
    i = input("Escolha o número da música para exibir as informações: ")
    caminho = (diretorio_raiz + "/" + str(i) + ".wav")
    arquivo_escolhido = wave.open(caminho,'r')

    escolha_do_usuário = int(input("Pressione para exibir: 1 para Número de Canais, 2 para Largura de Amostragem, 3 para Taxa Periódica de Quadros, 4 para Número de Quadros: "))

    # Definindo escolhas do usuário
    if escolha_do_usuário == 1:
        print( "Número de Canais: ",arquivo_escolhido.getnchannels())
    elif escolha_do_usuário == 2: 
        print ( "Largura de Amostragem: ",arquivo_escolhido.getsampwidth())
    elif escolha_do_usuário == 3:
        print ( "Taxa Periódica de Quadros: ",arquivo_escolhido.getframerate())
    elif escolha_do_usuário == 4:
        print ("Número de Quadros: ",arquivo_escolhido.getnframes())
    arquivo_escolhido.close()



diretorio_raiz = busca_wav()
converte_para_wav()
renomeia_wav()
plota_grafico()
learn_audio()

# Agradecimentos: #

# Ao Diretor de Desenvolvimento da TITAN - Computação Inteligente, João Paulo Rios. #
# Ao Professor de Introdução à Engenharia de Computação, Antônio Lopes #
