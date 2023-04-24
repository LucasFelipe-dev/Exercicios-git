import math

raio = float(input("Digite o valor do raio da esfera: "))
pi = 3.14159

volume = (4/3) * pi * math.pow(raio, 3)

print("O volume da esfera é:", round(volume, 3))