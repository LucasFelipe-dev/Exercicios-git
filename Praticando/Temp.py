temp = float(input('Inserir a temperatura do paciente: '))
if temp >= 39:
    print('Febre alta sua temperatura é {}'.format(temp))
elif temp > 39 and temp >= 37:
    print('Você está sem febre')
