#Questão 9) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma sequência em
#P.G. contendo 10 valores.


a = int(input("Digite o valor inicial A: "))
r = int(input("Digite a razão da R: "))

for i in range(10):
    print(a)
    a *= r
