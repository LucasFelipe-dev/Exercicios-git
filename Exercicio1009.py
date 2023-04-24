nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas efetuadas (em dinheiro): "))

comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao

print("O vendedor {} receberá R$ {:.2f} no final do mês.".format(nome, total_receber))
