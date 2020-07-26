import math

# Reto #4 - Calcular área de un círculo

"""Solicita a tu usuario que ingrese un número el cual será el radio de un círculo y con este dato calcula el área de un círculo.
Si tu lenguaje cuenta con librerías específicas para este propósito haz uso de las mismas."""

ratio = int(
    input('Ingresa un número que servirá para medir el área de un circulo: '))
res = math.pi * math.pow(ratio, 2)
print('\nEste es el resultado: %.2f' % res)
