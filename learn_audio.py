import wave

caminho = input("Insira o caminho do arquivo: ")

# Definindo input do arquivo

arquivo_escolhido = wave.open(caminho,'r')

print("INTRODUÇÃO À ENGENHARIA DE COMPUTAÇÃO")

print("BEM VINDO AO IDENTIFICADOR DE ÁUDIO!")

escolha_do_usuário=int(input("Pressione para exibir: 1 para Número de Canais, 2 para Largura de Amostragem, 3 para Taxa Periódica de Quadros, 4 para Número de Quadros: "))

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
