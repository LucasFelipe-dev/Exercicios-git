numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor recebido por hora: "))

salario = horas_trabalhadas * valor_hora

print(f"Funcionário número {numero_funcionario}")
print(f"Salário: R$ {salario:.2f}")