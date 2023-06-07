from random import *
import time
import os
from emoji import *
import winsound

# Grid
largura = 20
altura = 10

# Pacman
pacmin = 'o'
comida = 'X'
pacman = 'O'

# Função para gerar uma nova posição aleatória
def posicao():
    return [randint(0, 9), randint(0, 19)]

# Função para exibir o grid
def exibir_grid():
    for linha in range(altura):
        for coluna in range(largura):
            if [linha, coluna] == posicao_pacman:
                if exibir_pacmin:
                    print(pacmin, end='')
                else:
                    print(pacman, end='')
            elif [linha, coluna] == posicao_comida:
                print(comida, end='')
            else:
                print('.', end='')
        print()

# Loop principal do jogo
exibir_pacmin = True  # Variável auxiliar para controlar qual personagem exibir
posicao_pacman = posicao()
posicao_comida = posicao()

while True:
    # Limpar a tela
    os.system('cls')
    # Exibir o grid
    exibir_grid()

    # Verificar se o Pacman encontrou a comida
    if posicao_pacman == posicao_comida:
        # Gerar o beep
        winsound.Beep(frequency= 3000, duration= 50)
        print(emojize('\U0001f60b'))
        # Gerar novas posições para o pacmin e comida
        posicao_pacman = posicao()
        posicao_comida = posicao()
        exibir_pacmin = not exibir_pacmin

    # Atualizar a posição do Pacman automaticamente
    if posicao_pacman[0] < posicao_comida[0]:
        posicao_pacman[0] += 1
    elif posicao_pacman[0] > posicao_comida[0]:
        posicao_pacman[0] -= 1
    elif posicao_pacman[1] < posicao_comida[1]:
        posicao_pacman[1] += 1
    elif posicao_pacman[1] > posicao_comida[1]:
        posicao_pacman[1] -= 1

    # Aguardar um tempo para exibir o próximo frame (0.6 segundos neste exemplo)
    time.sleep(0.6)
