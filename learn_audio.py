import wave
obj = wave.open('audio.wav','r')

print("INTRODUÇÃO À ENGENHARIA DE COMPUTAÇÃO")

print("BEM VINDO AO IDENTIFICADOR DE ÁUDIO!")

escolha_do_usuário=int(input("Pressione para exibir: 1 para Número de Canais, 2 para Largura de Amostragem, 3 para Taxa Periódica de Quadros, 4 para Número de Quadros: "))

if escolha_do_usuário == 1:
    print( "Número de Canais: ",obj.getnchannels())

elif escolha_do_usuário == 2: 
    print ( "Largura de Amostragem: ",obj.getsampwidth())

elif escolha_do_usuário == 3:
    print ( "Taxa Periódica de Quadros: ",obj.getframerate())

elif escolha_do_usuário == 4:
    print ("Número de Quadros: ",obj.getnframes())
obj.close()
