# Questão 7) Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de N. 
#Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N.

n = int(input("Insira um valor entre 1 e 10 para calcular a tabuada: "))

if n < 1 or n > 10:
    print("O valor é invalido!!!")
else:
    for i in range (11):
        resultado = i * n 
        print("{} x {} = {}".format(i,n,resultado))       