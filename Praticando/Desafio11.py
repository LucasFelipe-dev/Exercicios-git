print('Programa para calcular o tamanho de uma parede e informar a quantidade de tinta que irá precisar!')
altura=float(input('Informe a altura m² da parede: '))
largura=float(input('Informe a largura m² da parede: '))
area=altura*largura/2
tinta=area/2
print(f'Uma parede tem {area:.3f}m² e você irá precisar de {tinta:.3f} litros de tinta para pinta-la!')