nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a srgunda nota: '))
media = (nota1 + nota2)/2
if media == 10:
    print(f'Aprovado com nota máxima: {media}')
elif media >= 7:
    print(f'Aprovado por média: {media}')
else:
    print(f'Reprovado, nota: {media}')