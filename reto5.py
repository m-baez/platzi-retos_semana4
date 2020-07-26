import math

# Reto #5 - Calcular volumen de un cilindro

"""Pide a tu usuario que indique el radio y la profundidad de un cilindro. Después aplica la fórmula correspondiente para calcular el volumen del cilindro y reduce el resultado a un solo decimal."""

ratio = int(input('Indica el radio de un cilindro: '))
depth = int(input('Ahora indica la profundidad: '))
res = math.pi * math.pow(ratio, 2) * depth

print('\nEste es el resultado: %.1f' % res)
