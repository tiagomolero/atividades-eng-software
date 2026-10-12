import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Missão Espacial - Defenda a Galáxia")

# Cores
COR_FUNDO = (10, 10, 35)
COR_NAVE = (80, 200, 255)
COR_CHAMA = (255, 165, 0)
COR_TIRO = (255, 255, 0)
COR_INIMIGO = (255, 70, 90)

# Configurações das estrelas
quantidade_estrelas = 80
estrelas = []

# Cria estrelas com velocidades diferentes
for i in range(quantidade_estrelas):

    estrela_x = random.randint(0, LARGURA - 1)
    estrela_y = random.randint(0, ALTURA - 1)

    tamanho = random.randint(1, 2)
    velocidade = random.uniform(0.5, 2.0)

    estrelas.append(
        [estrela_x, estrela_y, tamanho, velocidade]
    )

# Configurações da nave
nave_x = 400
nave_y = 450
velocidade_nave = 5

# Configurações dos tiros
tiros = []
velocidade_tiro = 8
largura_tiro = 6
altura_tiro = 18

intervalo_disparo = 250
ultimo_disparo = -intervalo_disparo

# Configurações dos inimigos
inimigos = []
velocidade_inimigo = 3
largura_inimigo = 50
altura_inimigo = 40

# Intervalo entre o surgimento dos inimigos
intervalo_inimigos = 1000
ultimo_inimigo = pygame.time.get_ticks()

# Controle do jogo
executando = True
relogio = pygame.time.Clock()

# Controle da tela atual
estado_jogo = "menu"

# Fontes do menu
fonte_titulo = pygame.font.SysFont("Arial", 52, bold=True)
fonte_menu = pygame.font.SysFont("Arial", 30)
fonte_instrucoes = pygame.font.SysFont("Arial", 24)

# Pontuação do jogador
pontuacao = 0

# Meta necessária para vencer
meta_pontos = 200

# Controle da condição de vitória
vitoria = False

# Fonte utilizada para exibir os pontos
fonte = pygame.font.SysFont("Arial", 28)

# Sistema de vidas
vidas = 3
game_over = False

# Tempo de invulnerabilidade após receber dano
ultimo_dano = -2000
tempo_invulneravel = 2000

# Fonte para a mensagem de derrota
fonte_game_over = pygame.font.SysFont("Arial", 60, bold=True)

# Função responsável pelo fundo espacial
def desenhar_fundo():

    # Preenche a tela com a cor do espaço
    tela.fill(COR_FUNDO)

    # Desenha as estrelas
    for estrela in estrelas:

        estrela_x = estrela[0]
        estrela_y = estrela[1]
        tamanho = estrela[2]

        pygame.draw.circle(
            tela,
            (200, 200, 255),
            (int(estrela_x), int(estrela_y)),
            tamanho
        )

# Atualiza a posição das estrelas
def atualizar_estrelas():

    for estrela in estrelas:

        # Move a estrela para baixo
        estrela[1] += estrela[3]

        # Quando sair da tela, volta para o topo
        if estrela[1] >= ALTURA:

            estrela[0] = random.randint(0, LARGURA - 1)
            estrela[1] = 0

# Função responsável pelo menu inicial
def desenhar_menu():

    desenhar_fundo()

    # Título principal
    titulo = fonte_titulo.render(
        "MISSÃO ESPACIAL",
        True,
        (80, 200, 255)
    )

    subtitulo = fonte_menu.render(
        "Defenda a Galáxia",
        True,
        (255, 255, 255)
    )

    tela.blit(
        titulo,
        titulo.get_rect(center=(LARGURA // 2, 120))
    )

    tela.blit(
        subtitulo,
        subtitulo.get_rect(center=(LARGURA // 2, 175))
    )

    # Comando para iniciar
    iniciar = fonte_menu.render(
        "PRESSIONE ENTER PARA JOGAR",
        True,
        (80, 255, 150)
    )

    tela.blit(
        iniciar,
        iniciar.get_rect(center=(LARGURA // 2, 280))
    )

    # Título da seção de controles
    titulo_controles = fonte_menu.render(
        "CONTROLES",
        True,
        (80, 200, 255)
    )

    tela.blit(
        titulo_controles,
        titulo_controles.get_rect(center=(LARGURA // 2, 355))
    )

    # Comandos organizados em duas colunas
    controles = [
        ("SETAS", "Movimentar nave"),
        ("ESPAÇO", "Atirar"),
        ("ESC", "Voltar ao menu")
    ]

    for indice, (tecla, acao) in enumerate(controles):

        posicao_y = 405 + indice * 38

        texto_tecla = fonte_instrucoes.render(
            tecla,
            True,
            (80, 200, 255)
        )

        texto_acao = fonte_instrucoes.render(
            acao,
            True,
            (255, 255, 255)
        )

        # Coluna esquerda: tecla
        tela.blit(texto_tecla, (210, posicao_y))

        # Coluna direita: ação
        tela.blit(texto_acao, (360, posicao_y))

    # Objetivo do jogo
    objetivo = fonte_instrucoes.render(
        "OBJETIVO: ALCANÇAR 200 PONTOS",
        True,
        (80, 255, 150)
    )

    tela.blit(
        objetivo,
        objetivo.get_rect(center=(LARGURA // 2, 550))
    )

# Função responsável por reiniciar a partida
def reiniciar_jogo():
    global nave_x, nave_y
    global tiros, inimigos
    global pontuacao, vidas
    global game_over, vitoria
    global ultimo_disparo, ultimo_inimigo, ultimo_dano
    global estado_jogo

    # Restaura a posição da nave
    nave_x = 400
    nave_y = 450

    # Remove tiros e inimigos anteriores
    tiros = []
    inimigos = []

    # Restaura pontuação e vidas
    pontuacao = 0
    vidas = 3

    # Limpa as condições de fim de jogo
    game_over = False
    vitoria = False

    # Reinicia os temporizadores
    tempo_atual = pygame.time.get_ticks()
    ultimo_disparo = tempo_atual - intervalo_disparo
    ultimo_inimigo = tempo_atual
    ultimo_dano = tempo_atual - tempo_invulneravel

    # Inicia uma nova partida
    estado_jogo = "jogando"

# Loop principal
while executando:

    # Verifica os eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.KEYDOWN:

            # Inicia uma partida nova pelo menu
            if estado_jogo == "menu":

                if evento.key == pygame.K_RETURN:
                    reiniciar_jogo()

            # Retorna ao menu durante a partida
            elif estado_jogo == "jogando":

                if evento.key == pygame.K_ESCAPE:
                    estado_jogo = "menu"

            # Reinicia após vitória ou derrota
            if vitoria or game_over:

                if evento.key == pygame.K_r:
                    reiniciar_jogo()

    # Atualiza a animação do fundo espacial
    atualizar_estrelas()

    # Verifica as teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Exibe o menu enquanto a partida não começou
    if estado_jogo == "menu":

        desenhar_menu()

        pygame.display.flip()
        relogio.tick(60)

        continue

    # Exibe a tela de vitória
    if vitoria:

        desenhar_fundo()

        texto_vitoria = fonte_game_over.render(
            "MISSÃO CUMPRIDA!",
            True,
            (80, 255, 150)
        )

        texto_final = fonte.render(
            f"Pontuação final: {pontuacao}",
            True,
            (255, 255, 255)
        )

        tela.blit(
            texto_vitoria,
            texto_vitoria.get_rect(
                center=(LARGURA // 2, ALTURA // 2 - 30)
            )
        )

        tela.blit(
            texto_final,
            texto_final.get_rect(
                center=(LARGURA // 2, ALTURA // 2 + 40)
            )
        )

        # Instrução para reiniciar
        texto_reiniciar = fonte.render(
            "Pressione R para jogar novamente",
            True,
            (80, 200, 255)
        )

        tela.blit(
            texto_reiniciar,
            texto_reiniciar.get_rect(
                center=(LARGURA // 2, ALTURA // 2 + 100)
            )
        )

        pygame.display.flip()
        relogio.tick(60)
        continue

    # Interrompe as atualizações da partida após a derrota
    if game_over:
        desenhar_fundo()

        texto_derrota = fonte_game_over.render(
            "GAME OVER",
            True,
            (255, 70, 90)
        )

        texto_final = fonte.render(
            f"Pontuação final: {pontuacao}",
            True,
            (255, 255, 255)
        )

        tela.blit(
            texto_derrota,
            texto_derrota.get_rect(
                center=(LARGURA // 2, ALTURA // 2 - 30)
            )
        )

        tela.blit(
            texto_final,
            texto_final.get_rect(
                center=(LARGURA // 2, ALTURA // 2 + 40)
            )
        )

        # Instrução para reiniciar
        texto_reiniciar = fonte.render(
            "Pressione R para jogar novamente",
            True,
            (80, 200, 255)
        )

        tela.blit(
            texto_reiniciar,
            texto_reiniciar.get_rect(
                center=(LARGURA // 2, ALTURA // 2 + 100)
            )
        )

        pygame.display.flip()
        relogio.tick(60)
        continue

    # Movimentação da nave
    if teclas[pygame.K_LEFT]:
        nave_x -= velocidade_nave

    if teclas[pygame.K_RIGHT]:
        nave_x += velocidade_nave

    if teclas[pygame.K_UP]:
        nave_y -= velocidade_nave

    if teclas[pygame.K_DOWN]:
        nave_y += velocidade_nave

    # Impede a nave de sair da janela
    nave_x = max(25, min(nave_x, LARGURA - 25))
    nave_y = max(0, min(nave_y, ALTURA - 95))

    tempo_atual = pygame.time.get_ticks()

    # Sistema de disparos
    if teclas[pygame.K_SPACE]:
        if tempo_atual - ultimo_disparo >= intervalo_disparo:

            novo_tiro = pygame.Rect(
                nave_x - largura_tiro // 2,
                nave_y - altura_tiro,
                largura_tiro,
                altura_tiro
            )

            tiros.append(novo_tiro)
            ultimo_disparo = tempo_atual

    # Atualiza os tiros
    for tiro in tiros[:]:
        tiro.y -= velocidade_tiro

        if tiro.bottom < 0:
            tiros.remove(tiro)

    # Cria novos inimigos
    if tempo_atual - ultimo_inimigo >= intervalo_inimigos:

        posicao_x = random.randint(
            0, LARGURA - largura_inimigo
        )

        novo_inimigo = pygame.Rect(
            posicao_x,
            -altura_inimigo,
            largura_inimigo,
            altura_inimigo
        )

        inimigos.append(novo_inimigo)
        ultimo_inimigo = tempo_atual

    # Movimenta os inimigos
    for inimigo in inimigos[:]:
        inimigo.y += velocidade_inimigo

        # Remove inimigos que saíram da tela
        if inimigo.top > ALTURA:
            inimigos.remove(inimigo)

    # Detecta colisões entre tiros e inimigos
    for tiro in tiros[:]:
        for inimigo in inimigos[:]:

            if tiro.colliderect(inimigo):

                # Remove o inimigo atingido
                inimigos.remove(inimigo)

                # Remove o tiro
                tiros.remove(tiro)

                # Adiciona pontos ao jogador
                pontuacao += 10

                # Verifica se o jogador venceu
                if pontuacao >= meta_pontos:
                    vitoria = True

                # Encerra a verificação deste tiro
                break

    # Verifica colisões dos inimigos com o jogador
    if not game_over:

        nave_rect = pygame.Rect(
            nave_x - 25,
            nave_y,
            50,
            70
        )

        for inimigo in inimigos[:]:

            if nave_rect.colliderect(inimigo):

                if tempo_atual - ultimo_dano >= tempo_invulneravel:

                    vidas -= 1
                    ultimo_dano = tempo_atual

                    # Remove o inimigo que causou dano
                    inimigos.remove(inimigo)

                    # Verifica a condição de derrota
                    if vidas <= 0:
                        game_over = True

                    break

    # Desenha o fundo
    desenhar_fundo()

    # Desenha a nave do jogador
    pygame.draw.polygon(
        tela,
        COR_NAVE,
        [
            (nave_x, nave_y),
            (nave_x - 25, nave_y + 70),
            (nave_x + 25, nave_y + 70)
        ]
    )

    # Desenha a chama
    pygame.draw.polygon(
        tela,
        COR_CHAMA,
        [
            (nave_x - 10, nave_y + 70),
            (nave_x, nave_y + 95),
            (nave_x + 10, nave_y + 70)
        ]
    )

    # Desenha os tiros
    for tiro in tiros:
        pygame.draw.rect(tela, COR_TIRO, tiro)

    # Desenha as naves inimigas
    for inimigo in inimigos:
        pygame.draw.polygon(
            tela,
            COR_INIMIGO,
            [
                (inimigo.centerx, inimigo.bottom),
                (inimigo.left, inimigo.top),
                (inimigo.right, inimigo.top)
            ]
        )

    # Exibe a pontuação na tela
    texto_pontos = fonte.render(
        f"Pontos: {pontuacao}",
        True,
        (255, 255, 255)
    )

    tela.blit(texto_pontos, (10, 10))

    # Exibe a quantidade de vidas
    texto_vidas = fonte.render(
        f"Vidas: {vidas}",
        True,
        (255, 100, 100)
    )

    tela.blit(texto_vidas, (LARGURA - 130, 10))

    # Atualiza a tela
    pygame.display.flip()

    # Limita a 60 FPS
    relogio.tick(60)

# Finaliza o Pygame
pygame.quit()