# Código Python generado automáticamente por TurismoLang

import sys

def inicio():
    print('Visita guiada')
    opcion = input('Restaurante -> ')
    if opcion == 'Restaurante':
        return restaurante()
    print('Opción no reconocida, intenta de nuevo.')
    return inicio()

def restaurante():
    print('Comida típica')
    opcion = input('Volver -> ')
    if opcion == 'Volver':
        return inicio()
    print('Opción no reconocida, intenta de nuevo.')
    return restaurante()

if __name__ == '__main__':
    inicio()