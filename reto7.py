import math

# Reto #7 - Calcular perímetros y áreas

"""Muestra un menú con distintas figuras geométricas, por lo menos 3 diferentes (triángulo, cuadrado, pentágono, etc.)
Tu usuario debe poder elegir alguna de estas figuras, indicar la distancia de sus lados y mostrar como resultado tanto el perímetro como el área de dicha figura."""


def options():
    print('-', '- '*17)
    print("|    Elige una opción disponible   |")
    print("|    1. Triángulo equilatero       |")
    print("|    2. Triángulo isoseles         |")
    print("|    3. Tríangulo escaleno         |")
    print("|    4. Cuadrado                   |")
    print("|    5. Pentágono                  |")
    print("|                                  |")
    print("|    0. Salir                      |")
    print(' -'*17, '-')


def equilateralTriangle():
    side = float(input('¿Cuánto mide el lado del tríangulo en cm? '))
    calcSquare = math.pow(side, 2) - math.pow(side/2, 2)
    heigth = math.sqrt(calcSquare)
    triangleArea = (side * heigth) / 2
    print('\nEste es el perimetro: %.2fcm' % (side*3))
    print('Y esta es el área: %.2fcm' % triangleArea)


def triangle():
    pass


def menu():
    while True:
        options()
        try:
            userInput = int(input("Seleccione una opcion: "))
            if userInput in range(6):
                if userInput == 0:
                    print("Adios! Vuelva pronto")
                    break
                elif userInput == 1:
                    equilateralTriangle()
                    break
                print("\nHas elegido la opción %d\n" % userInput)
            else:
                print('Error, solo de aceptan numeros del 0 al 5')
        except ValueError:
            print("Error, ingrese solamente numeros")


if __name__ == '__main__':
    menu()
