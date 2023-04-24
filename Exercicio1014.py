distancia_total = float(input("Digite a distância total percorrida em Km: "))
total_combustivel = float(input("Digite o total de combustível gasto em litros: "))

consumo_medio = distancia_total / total_combustivel

print("O consumo médio é:", round(consumo_medio, 2))
