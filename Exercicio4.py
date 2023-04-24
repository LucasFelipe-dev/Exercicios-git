# Questão 4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos
# deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deve terminar quando for lido um número negativo
qtd_0_25 = 0
qtd_26_50 = 0
qtd_51_75 = 0
qtd_76_100 = 0

while True:
    valor = int(input("Digite um valor (digite um número negativo para sair): "))
    
    if valor < 0:
        break
    
    if valor >= 0 and valor <= 25:
        qtd_0_25 += 1
    elif valor >= 26 and valor <= 50:
        qtd_26_50 += 1
    elif valor >= 51 and valor <= 75:
        qtd_51_75 += 1
    elif valor >= 76 and valor <= 100:
        qtd_76_100 += 1
print("Quantidade de números no intervalo 0-25: ", qtd_0_25)
print("Quantidade de números no intervalo 26-50: ", qtd_26_50)
print("Quantidade de números no intervalo 51-75: ", qtd_51_75)
print("Quantidade de números no intervalo 76-100: ", qtd_76_100)
