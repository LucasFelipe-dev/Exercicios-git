# Questão 5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos.
# O número que encerrará a leitura será zero.

qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_geral = 0

while True:
    numero = int(input("Digite um número ou 0 zero para sair: "))

    if numero != 0:
        if numero %2 == 0:
            qtd_pares += 1
            soma_pares += numero
        else:
            qtd_impares += 1
        soma_geral += numero
    else:
        break
    if qtd_pares > 0:
        media_par =soma_pares / qtd_pares
    else:
        media_par = 0
    if soma_geral > 0:
        media_geral = soma_geral / (qtd_pares + qtd_impares)
    else:
        media_geral = 0

print("Quantidade de números pares: ", qtd_pares)
print("Quantidade de números ímpares: ", qtd_impares)
print("Média dos valores pares: ", media_par)
print("Média geral dos números não lidos: ", media_geral)