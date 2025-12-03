//DUPLA: GABRIELE MARIA FREIBERGER E BEATRICE FISCHER.

#include <stdio.h>
#include <stdlib.h>

int main (void) {
    //variáveis
    char t[3][3], jogador_atual = 'X', simbolo_jogador[3];
    int jogada_valida, jogadas_restantes, vencedor, continuar_jogo, i, j;

    simbolo_jogador[1] = 'X';
    simbolo_jogador[2] = 'O';

    do { //múltiplas partidas

        jogadas_restantes = 9;
        vencedor = 0;

        //cria o tabuleiro
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                t[i][j] = ' ';
            }
        }
        jogador_atual = 'X'; //jogador 1 comeca

        while (jogadas_restantes > 0 && vencedor == 0) {

            //mostra o tabuleiro
            printf("JOGO DA VELHA \n\n");
            printf("  0   1   2\n");
            for ( int i = 0; i < 3; i++) {
                printf("%i", i);
                for (int j = 0; j < 3; j++) {
                    printf(" %c ", t[i][j]);
                    if (j < 2) {
                        printf("|");
                    }
                }
                printf("\n");
                if (i < 2) {
                    printf(" ---|---|---\n");
                }
            }
            printf("\n----------------------\n\n");

            //validar a jogada
            jogada_valida = 0;
            while (jogada_valida == 0) {
                printf("Jogador %c, digite a linha (0 2) e coluna (0 2) colocando um espaco entre os numeros: ", jogador_atual);
				scanf("%i %i",&i,&j);
				
				//erro: numero invalido
                if ((i < 0 || i > 2) && (j < 0 || j > 2)) {
                    printf("Entrada invalida. Tente novamente.\n");
                    fflush(stdin);
                }
                //erro: caracter invalido
                if ((i < 'a' || i > 'z') && (j < 'a' || j > 'z') && (i < 'A' || i > 'Z') && (j < 'A' || j > 'Z')) {
                    printf("Entrada invalida. Tente novamente.\n");
                    fflush(stdin);
                }
                
                //erro: fora da matriz
                if (i < 0 || i > 2 || j < 0 || j > 2) {
                    printf("Posicao fora do tabuleiro. Tente novamente.\n");
                } 
                //erro: posição ocupada
                else if (t[i][j] != ' ') {
                    printf("Posicao ocupada. Tente novamente.\n");
                } 
                else {
                    jogada_valida = 1;
                    system("cls");
                }
            }

            //conta a jogada
            t[i][j] = jogador_atual;
            jogadas_restantes--;

            //verifica vitória
            for (int i = 0; i < 3; i++) {
                if (t[i][0] == t[i][1] && t[i][1] == t[i][2] && t[i][0] != ' ') {
                    if (jogador_atual == 'X') {
					    vencedor = 1;
					} else {
					    vencedor = 2;
					}
                }
                if (t[0][i] == t[1][i] && t[1][i] == t[2][i] && t[0][i] != ' ') {
                    if (jogador_atual == 'X') {
    					vencedor = 1;
					} else {
					    vencedor = 2;
					}
                }
            }
            
            if (vencedor != 0) {
            }
            // verifica a diagonal principal
            else if (t[0][0] == t[1][1] && t[1][1] == t[2][2] && t[0][0] != ' ') {
                if (jogador_atual == 'X') {
				    vencedor = 1;
				} else {
				    vencedor = 2;
				}
            }
            // verifica diagonal secundaria
            else if (t[0][2] == t[1][1] && t[1][1] == t[2][0] && t[0][2] != ' ') {
                if (jogador_atual == 'X') {
				    vencedor = 1;
				} else {
				    vencedor = 2;
				}
            }

            //troca o jogador se der velha
            if (vencedor == 0) {
             	if (jogador_atual == 'X') {
             		jogador_atual = 'O';
				 } else {
				 	jogador_atual = 'X';
				 }
            }
        }

        // tabuleiro final
        printf("\n RESULTADO \n\n");
        printf("  0   1   2\n");
        for (int i = 0; i < 3; i++) {
            printf("%i", i);
            for (int j = 0; j < 3; j++) {
                printf(" %c ", t[i][j]);
                if (j < 2) {
                    printf("|");
                }
            }
            printf("\n");
            if (i < 2) {
                printf(" ---|---|---\n");
            }
        }
        printf("\n----------------------------------------------------\n");

        //resultado do jogo
        if (vencedor == 1) {
            printf("\nParabens! O Jogador X Venceu!\n");
        } else if (vencedor == 2) {
            printf("\nParabens! O Jogador O Venceu!\n");
        } else {
            printf("\nDEU VELHA!\n");
        }
        
        // Pergunta se deseja jogar novamente
        printf("\nDeseja jogar novamente? (1 para Sim / 0 para Nao): ");
        if (scanf("%i", &continuar_jogo) != 1) {
            printf("Entrada invalida. O programa sera finalizado.\n");
            continuar_jogo = 0;
            fflush(stdin);
        }

    } while (continuar_jogo == 1);

    printf("Fim do jogo. Obrigado por jogar!\n");
    return 0;
}
