# Temperatura do usuario
C = float(input('Digite a temperatura em graus Celcius: '))

# Converssão de medida
F = (C * (9/5)) + 32
K = C + 273.15

# Impressão das novas medidas
print('Em Fahrenheit, a temperatura mostrada é de ', F, 'ºF', sep='')
print('Em Kelvin, ', K, 'ºK', sep='')
