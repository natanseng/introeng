import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
import os
from pydub import AudioSegment
import wave


musicas_mp3 = list()
musicas_wav = list()


#essa função busca um arquivo e coloca em uma lista

def busca_wav():
    diretorio_raiz = input('Qual diretório deseja buscar os arquivos .WAV? ')
    for file in os.listdir(diretorio_raiz):
        if file.endswith(".wav"):
            musicas_wav.append(str(file))
        elif file.endswith(".mp3"):
            musicas_mp3.append(str(file))

#essa função converte arquivos de mp3 da lista em wav e os muda de lista

def converte_para_wav():
    for musica in musicas_mp3:
        sound = AudioSegment.from_mp3(musica)
        sound.export(musica.replace('.mp3', '.wav'), format="wav")
        musicas_wav.append(musica.replace('.mp3', '.wav'))
        
        
def renomeia_wav():
    cont = 1
    for musica in musicas_wav:
        musica = (musica.replace(recupera_nome_musica(musica), str(cont)))
        cont = cont + 1

def recupera_nome_musica(musica):
    partes = musica.split('\\')
    return partes[len(partes) - 1]

#as duas funções a cima renomeio os arquivos .wav

def carregar_wave():
    pass


def plota_grafico(musica):
    pass

def downmixing(musica):
    pass
