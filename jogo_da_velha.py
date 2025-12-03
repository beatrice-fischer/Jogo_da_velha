import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("\nJOGO DA VELHA\n")
    print("   0   1   2")
    for i in range(3):
        print(f"{i}", end="")
        for j in range(3):
            print(f" {tabuleiro[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print(" ---|---|---")
    print("\n----------------------\n")

# Função para verificar se há um vencedor
def verificar_vitoria(tabuleiro, jogador):
    # Condições de vitória 
    vitorias = [
        # Linhas
        [tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]],
        [tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]],
        [tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]],
        # Colunas
        [tabuleiro[0][0], tabuleiro[1][0], tabuleiro[2][0]],
        [tabuleiro[0][1], tabuleiro[1][1], tabuleiro[2][1]],
        [tabuleiro[0][2], tabuleiro[1][2], tabuleiro[2][2]],
        # Diagonais
        [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]],
        [tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]]
    ]
    
    # Verifica se qualquer uma das listas de vitória contém apenas o símbolo do jogador
    for linha_ou_coluna_ou_diagonal in vitorias:
        if all(simbolo == jogador for simbolo in linha_ou_coluna_ou_diagonal):
            return True
            
    return False

# Função principal do jogo
def jogar_jogo_da_velha():
    continuar_jogo = 1
    
    while continuar_jogo == 1:
        # Inicialização do tabuleiro com compreensão de lista
        tabuleiro = [[' '] * 3 for _ in range(3)] 
        jogador_atual = 'X'
        jogadas_restantes = 9
        vencedor = False

        limpar_tela()
        
        while jogadas_restantes > 0 and not vencedor:
            exibir_tabuleiro(tabuleiro)
            jogada_valida = False
            
            # Loop para obter e validar a jogada
            while not jogada_valida:
                try:
                    entrada = input(f"Jogador {jogador_atual}, digite a linha e coluna (ex: 0 2): ").split()
                    
                    if len(entrada) != 2:
                        print("Entrada inválida. Digite exatamente dois números separados por espaço.")
                        continue
                        
                    linha = int(entrada[0])
                    coluna = int(entrada[1])
                    
                    if not (0 <= linha <= 2 and 0 <= coluna <= 2):
                        print("Posição fora do tabuleiro (deve ser entre 0 e 2). Tente novamente.")
                    elif tabuleiro[linha][coluna] != ' ':
                        print("Posição ocupada. Tente novamente.")
                    else:
                        jogada_valida = True
                        limpar_tela() 
                        
                except ValueError:
                    print("Entrada inválida. Por favor, digite apenas números inteiros para linha e coluna.")

            # Executa a jogada
            tabuleiro[linha][coluna] = jogador_atual
            jogadas_restantes -= 1
            
            # Verifica vitória
            if verificar_vitoria(tabuleiro, jogador_atual):
                vencedor = True
            
            # Troca de jogador com operador ternário 
            if not vencedor:
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        # Resultado da partida
        exibir_tabuleiro(tabuleiro)
        print("----------------------------------------------------\n")

        if vencedor:
            print(f"\nParabéns! O Jogador {jogador_atual} Venceu!\n")
        else:
            print("\nDEU VELHA!\n")
        
        # Pergunta se deseja jogar novamente
        while True:
            try:
                continuar_input = input("\nDeseja jogar novamente? (1 para Sim / 0 para Não): ")
                continuar_jogo = int(continuar_input)
                if continuar_jogo not in [0, 1]:
                    print("Opção inválida. Digite 1 ou 0.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite 1 ou 0.")
                
    print("\nFim do jogo. Obrigado por jogar!\n")

if __name__ == "__main__":
    jogar_jogo_da_velha()