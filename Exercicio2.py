#Questão 2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
#mostrar:
#a. A menor altura do grupo;
#b. A maior altura do grupo;

altura = []

for i in range (15):
    altura.append(float(input(f"Digite a altura da pessoa {i+1}: ")))
    maioralt = max(altura)
    menoralto = min(altura)

print("Maior altura é: ",maioralt)
print("Menor altura é: ",menoralto)