import math

# Reto #3 - Raíces cuadradas redondeadas

"""Pide a tu usuario que ingrese un número, cuyo valor debe ser mayor a 20, luego calcula su raíz cuadrada y reduce a 2 o 3 decimales el resultado final."""

number = int(
    input('Ingresa un número mayor a 20 para calcular su raíz cuadrada: '))
sRoot = math.sqrt(number)

if number < 20:
    print('\nPor favor ingresa un número mayor a 20')
else:
    print('\nEste es el resultado: %.2f' % sRoot)
