# Questão 3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos

soma = 0
qtd_positivos = 0
qtd_negativos = 0

while True:
    valor = float(input("Digite um valor ou digite 0 para sair/calcular: "))
    
    if valor == 0:
        break
    
    soma += valor
    
    if valor > 0:
        qtd_positivos += 1
    else:
        qtd_negativos += 1

media = soma / (qtd_positivos + qtd_negativos)

perc_positivos = (qtd_positivos / (qtd_positivos + qtd_negativos)) * 100
perc_negativos = (qtd_negativos / (qtd_positivos + qtd_negativos)) * 100

print("Média aritmética: ", media)
print("Quantidade de valores positivos: ", qtd_positivos)
print("Quantidade de valores negativos: ", qtd_negativos)
print("Percentual de valores positivos: ", perc_positivos, "%")
print("Percentual de valores negativos: ", perc_negativos, "%")