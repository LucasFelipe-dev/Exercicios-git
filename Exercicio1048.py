salario = float(input("Digite o salário do funcionário: "))

if salario <= 400:
    percentual = 15
elif salario <= 800:
    percentual = 12
elif salario <= 1200:
    percentual = 10
elif salario <= 2000:
    percentual = 7
else:
    percentual = 4

reajuste = salario * percentual / 100
novo_salario = salario + reajuste

print(f"Novo salário: R$ {novo_salario:.2f}")
print(f"Reajuste: R$ {reajuste:.2f}")
print(f"Índice de reajuste: {percentual}%")
