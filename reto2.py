#  Reto #2 - Reducir los decimales

"""Toma como base el reto anterior, pero ajústalo para que el resultado muestre solamente 1, 2, 3 o 4 decimales."""

n1 = float(input('Ingresa un número con decimales: '))
n2 = float(input('Ingresa orto número con decimales: '))
res = n1 * n2
print('Este es el resultado: %.2f' % res)
