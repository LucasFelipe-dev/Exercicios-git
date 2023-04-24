# Lê 3 valores reais
a, b, c = map(float, input().split())

# Verifica se formam um triângulo
if a + b > c and a + c > b and b + c > a:
    # Calcula o perímetro
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    # Calcula a área do trapézio
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")
