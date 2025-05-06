# Declaração dos termos da equação
a = float(2)  # Segundo grau
b = float(2)  # Primeiro grau
c = float(-4)  # Independente
# Mude o sinal de 'c' se quiser testar diferentes casos

# Termo dentro da raiz da fórmula de Bhaskara
delta = (b**2 - 4*a*c)

# Caso das raizes imaginarias
if (delta < 0):
    real = (-1*b) / (2*a)
    delta = delta * (-1)
    raizi = ((delta)**0.5) / (2*a)

    print('As raizes da equação de segundo grau mostrada são:')
    print(real, ' +', raizi, 'i', sep='')
    print(real, ' -', raizi, 'i', sep='')

# Caso de burrice de usuario
elif (a == 0):
    print("Essa é uma equação de primeiro grau \nFaz na mão isso ai (-_-')")

# Caso das raizes reais
else:
    raiz1 = (-1*b + (delta)**0.5) / (2*a)
    raiz2 = (-1*b - (delta)**0.5) / (2*a)

    print('As raizes da equação de segundo grau mostrada são', raiz1, 'e', raiz2)
