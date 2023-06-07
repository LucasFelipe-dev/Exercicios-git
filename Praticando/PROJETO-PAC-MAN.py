#Grid do pacman
import random

#Grid
largura = 15
altura = 10

#Pacman
pacmin = 'o'
comida = 'X'

#n = 15
#ponto = n*'.'
#matriz = []

#exibir o grid
def exibir_grid(grid):
    for linha in grid:
        print(' '.join(linha))


#Animaçao do pacman
    def animacaopacman (anime):
        if pacmin == 'o':
            return 'O'
        else:
            return 'o'
def jogar ():
    grid = [['.' for _ in range(largura)] for _ in range(altura)]

#posicionar o pacman
    pos_pacman = (random.randint(0, altura - 1), random.randint(0, largura - 1))
    pos_comida = (random.randint(0, altura - 1), random.randint(0, largura - 1))

# Atualizar o grid com o Pacman e a comida
    grid[pos_pacman[0]][pos_pacman[1]] = pacmin
    grid[pos_comida[0]][pos_comida[1]] = comida
#Loop do jogo
while True:
        print('\n'*10)
        exibir_grid()




#for i in range(1,10):
#    linha = list(ponto)
 #   pos_pacmin = choice(range(n))
  #  pos_comida = choice(range(n))
   # linha[pos_pacmin] = pacmin
   # linha[pos_comida] = comida
  #  matriz.append(linha)
#for linha in matriz:
 #   print(''.join(linha))