# DUPLA: GABRIELE MARIA FREIBERGER E BEATRICE FISCHER.

# Função para exibir o tabuleiro
def exibir_tabuleiro():
    print("\nJOGO DA VELHA\n")
    print("   0   1   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[2][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]))
    print("\n----------------------\n")

# Verificar vitória
def verificar_vitoria(rodada):
    global parar
    if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro[0][2] == rodada):
        exibir_tabuleiro()
        print("O jogador {} Venceu!".format(rodada))
        parar = True

    if(tabuleiro[1][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[1][2] == rodada):
        exibir_tabuleiro()
        print("O jogador {} Venceu!".format(rodada))
        parar = True

    if(tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][2] == rodada):
        exibir_tabuleiro()
        print("O jogador {} Venceu!".format(rodada))
        parar = True

    if(tabuleiro[0][0] == rodada and tabuleiro[1][0] == rodada and tabuleiro[2][0] == rodada):
        exibir_tabuleiro()
        print("O jogador {} Venceu!".format(rodada))
        parar = True

    if(tabuleiro[0][1] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][1] == rodada):
        exibir_tabuleiro()
        print("O jogador {} Venceu!".format(rodada))
        parar = True

    if(tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][2] == rodada):
        exibir_tabuleiro()
        print("O jogador {} Venceu!".format(rodada))
        parar = True

    if(tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][2] == rodada):
        exibir_tabuleiro()
        print("O jogador {} Venceu!".format(rodada))
        parar = True

tabuleiro = [[" "," "," "],[" "," "," "],[" "," "," "]]

# Funcionamento do jogo
parar = False
rodada = "X"
jogadas = 0

while parar == False:
    #Empate
    if jogadas == 9:
        exibir_tabuleiro()
        print("DEU VELHA!")
        parar = True 

    exibir_tabuleiro()

    i = int(input("Jogador, digite a linha: "))
    j = int(input("Jogador, digite a coluna: "))

    if rodada == "X":
        tabuleiro[i][j] = "X"
        verificar_vitoria(rodada)
        jogadas += 1
        rodada = "O"
    elif rodada == "O":
        tabuleiro[i][j] = "O"
        verificar_vitoria(rodada)
        jogadas += 1
        rodada = "X"

    

print("Fim do jogo. Obrigado por jogar!")


