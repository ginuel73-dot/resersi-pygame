import pygame
from game_logic import create_board, BLACK, WHITE, EMPTY

pygame.init()


LARGURA_TELA = 1920
ALTURA_TELA = 1080
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Meu Reversi")


TAMANHO_TABULEIRO = 8  
tabuleiro = create_board()  

tamanho_celula = ALTURA_TELA // TAMANHO_TABULEIRO
deslocamento_x = (LARGURA_TELA - (tamanho_celula * TAMANHO_TABULEIRO)) // 2
deslocamento_y = 0  

jogo_ativo = True
while jogo_ativo:
    # Preenche fundo verde
    tela.fill((0, 150, 0))

   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False


    for linha in range(TAMANHO_TABULEIRO):
        for coluna in range(TAMANHO_TABULEIRO):
            x = deslocamento_x + coluna * tamanho_celula
            y = deslocamento_y + linha * tamanho_celula


            pygame.draw.rect(tela, (0, 0, 0), (x, y, tamanho_celula, tamanho_celula), 2)


            if tabuleiro[linha][coluna] == BLACK:
                pygame.draw.circle(
                    tela,
                    (30, 30, 30),  # preto
                    (x + tamanho_celula // 2, y + tamanho_celula // 2),
                    int(tamanho_celula * 0.45)
                )

            elif tabuleiro[linha][coluna] == WHITE:
                pygame.draw.circle(
                    tela,
                    (230, 230, 230),  # branco
                    (x + tamanho_celula // 2, y + tamanho_celula // 2),
                    int(tamanho_celula * 0.45)
                )

   
    pygame.display.flip()

pygame.quit()
