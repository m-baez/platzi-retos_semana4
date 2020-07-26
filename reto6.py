# Reto #6 - Mostrar enteros y residuos

"""Pide al usuario que ingrese 2 números, divídelos, muestra un resultado como enteros y además el residuo por separado de una forma que seal fácil de entender al usuario.
Por ejemplo: “9 dividido entre 2 es 4 y sobra 1”."""

n1 = int(input('Por favor ingresa un número: '))
n2 = int(input('Ahora otro por favor: '))
res = n1 / n2
res2 = n1 % n2
print('\nEste es el resultado de dividir %d entre %d --> %d' % (n1, n2, res))
print('Y esto es lo que sobra de la division --> %d' % res2)
