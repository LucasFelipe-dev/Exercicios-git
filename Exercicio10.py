#Questão 10) Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

a = int(input("Digite um valor inteiro para imprimir sua sequencia: "))
fat = 1
print(f"{a}! = ", end='')

for i in range(a, 0, -1):
    print(i, end='')
    if i > 1:
        print(" x ", end='')
    else:
        print(" = ", end='')
    fat *= i

print(f"{fat}")
