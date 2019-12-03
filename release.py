def learn_audio(caminho):

        escolha_do_usuário=int(input("Pressione para exibir: 1 para Número de Canais, 2 para Largura de Amostragem, 3 para Taxa Periódica de Quadros, 4 para Número de Quadros: "))

    if escolha_do_usuário == 1:
        print( "Número de Canais: ",arquivo_escolhido.getnchannels())

    elif escolha_do_usuário == 2:
        print ( "Largura de Amostragem: ",arquivo_escolhido.getsampwidth())

    elif escolha_do_usuário == 3:
        print ( "Taxa Periódica de Quadros: ",arquivo_escolhido.getframerate())

    elif escolha_do_usuário == 4:
        print ("Número de Quadros: ",arquivo_escolhido.getnframes())
