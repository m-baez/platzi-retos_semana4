import math

# Reto #7 - Calcular perímetros y áreas

"""Muestra un menú con distintas figuras geométricas, por lo menos 3 diferentes (triángulo, cuadrado, pentágono, etc.)
Tu usuario debe poder elegir alguna de estas figuras, indicar la distancia de sus lados y mostrar como resultado tanto el perímetro como el área de dicha figura."""


def options():
    print(' -'*48)
    print("|    Calcula el perímetro y área de una de las siguientes figuras, elige una opción disponible   |".upper())
    print("|                                                                                                |")
    print("|    1.- Triángulo equilatero                                                                    |")
    print("|    2.- Triángulo isósceles                                                                     |")
    print("|    3.- Cuadrado                                                                                |")
    print("|    4.- Pentágono                                                                               |")
    print("|                                                                                                |")
    print("|    0.- Salir                                                                                   |")
    print(' -'*48)


def menu():
    print(' ='*22, '\n')
    print('    Elige una de las opciones disponibles   \n'.upper())
    print('    1.- Calcular de nuevo con valores distintos')
    print('    2.- Elegir otra figura')
    print('    0.- Salir')
    print('\n', ' ='*22)

    userInput = int(input("Seleccione una opción: "))

    if userInput == 0:
        print("\n¡Gracias por usar nuestra calculadora!")
    elif userInput == 1:
        equilateralTriangle()
    elif userInput == 2:
        main()


def equilateralTriangle():
    side = float(input('¿Cuánto mide el lado del tríangulo en cm? '))
    calcSquare = math.pow(side, 2) - math.pow(side/2, 2)
    heigth = math.sqrt(calcSquare)
    triangleArea = (side * heigth) / 2
    print('\nEste es el perímetro: %.2fcm' % (side*3))
    print('Y esta es el área: %.2fcm\n' % triangleArea)
    menu()


def isoscelesTriangle():
    sides = float(input('¿Cúanto miden los lados tu triángulo en cm? '))
    base = float(input('¿Y cúanto mide la base? '))
    calcSquare = math.pow(sides, 2) - math.pow(base/2, 2)
    heigth = math.sqrt(calcSquare)
    area = base * heigth / 2
    print('\nEste es el perímetro: %.2fcm' % ((sides*2)+base))
    print('Y esta es el área: %.2fcm\n' % area)
    menu()


def square():
    sides = float(input('¿Cúanto miden los lados de tu cuadrado? '))
    print('\nEste es el perímetro: %.2fcm' % (sides*4))
    print('Y esta es el área: %.2fcm\n' % math.pow(sides, 2))


def pentagon():
    sides = float(input('¿Cúanto miden los lados de tu pentágono? '))
    tangent = math.tan(math.radians(36)) * 2
    apothem = sides / tangent
    area = (5 * sides * apothem) / 2
    print('\nEste es el perímetro: %.2fcm' % (sides*5))
    print('Y esta es el área: %.2fcm\n' % area)


def main():
    while True:
        options()
        try:
            userInput = int(input("Seleccione una opción: "))
            if userInput in range(5):
                if userInput == 0:
                    print("\n¡Gracias por usar nuestra calculadora!")
                    break
                elif userInput == 1:
                    equilateralTriangle()
                    break
                elif userInput == 2:
                    isoscelesTriangle()
                    break
                elif userInput == 3:
                    square()
                    break
                elif userInput == 4:
                    pentagon()
                    break
            else:
                print('\nError, solo de aceptan numeros del 0 al 5')
        except ValueError:
            print("\nError, ingrese solamente numeros")


if __name__ == '__main__':
    main()
