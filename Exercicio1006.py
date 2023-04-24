a = float(input("Digite a primeira nota (peso 2): "))
b = float(input("Digite a segunda nota (peso 3): "))
c = float(input("Digite a terceira nota (peso 5): "))

media = (a*2 + b*3 + c*5) / 10

print(f"A média ponderada do aluno é: {media:.1f}")