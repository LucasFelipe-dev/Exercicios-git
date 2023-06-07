#Pesquisar preço de 3 produtos em locais distintos e informar o menor preço
nomeprod=input('Insira o produto que está comparando: ')
vlr1=float(input('Insira o primeiro valor: '))
vlr2=float(input('Insira o segundo valor: '))
vlr3=float(input('Insira o terceiro valor: '))
if vlr1 < vlr2 and vlr1 < vlr3:
    print(f'O produto informado foi {nomeprod} e o valor mais barato custa: {vlr1}')
elif vlr2 < vlr1 and vlr2 < vlr3:
    print(f'O produto informado foi {nomeprod} e o valor mais barato custa: {vlr2}')
else:
    print(f'O produto informado foi {nomeprod} e o valor mais barato custa: {vlr3}')