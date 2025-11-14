# Código Python generado automáticamente por TurismoLang

import sys

def inicio():
    print('Hola viajero')
    opcion = input('Ir al parque -> ')
    if opcion == 'Ir al parque':
        return parque()
    print('Opción no reconocida, intenta de nuevo.')
    return inicio()

def parque():
    print('Bienvenido al parque central')
    opcion = input('Ir al inicio -> ')
    if opcion == 'Ir al inicio':
        return inicio()
    print('Opción no reconocida, intenta de nuevo.')
    return parque()

if __name__ == '__main__':
    inicio()
    