from random import *

# Grid
largura = 20
altura = 10

#Pacman
pacmin = 'o'
comida = 'X'

# Posição inicial do Pacman
posicao_pacman = [randint(0,9),randint(0,19)]

# Posição inicial da comida
posicao_comida = [randint(0,9),randint(0,19)]

# Função para exibir o grid
def exibir_grid():
    for linha in range(altura):
        for coluna in range(largura):
            if [linha, coluna] == posicao_pacman:
                print(pacmin, end='')
            elif [linha, coluna] == posicao_comida:
                print(comida, end='')
            else:
                print('.', end='')
        print()

# Loop principal do jogo
while True:
    # Limpar a tela
    print('\033[H\033[J')
    # Exibir o grid
    exibir_grid()

    # Verificar se o Pacman encontrou a comida
    if posicao_pacman == posicao_comida:
        print("Encontrou a comida!")
        break

    # Atualizar a posição do Pacman automaticamente
    if posicao_pacman[0] < posicao_comida[0]:
        posicao_pacman[0] += 1
    elif posicao_pacman[0] > posicao_comida[0]:
        posicao_pacman[0] -= 1
    elif posicao_pacman[1] < posicao_comida[1]:
        posicao_pacman[1] += 1
    elif posicao_pacman[1] > posicao_comida[1]:
        posicao_pacman[1] -= 1

    # Aguardar um tempo para exibir o próximo frame (0.5 segundos neste exemplo)
    import time
    time.sleep(0.4)
