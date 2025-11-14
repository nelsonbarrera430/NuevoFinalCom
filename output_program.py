# Código generado automáticamente por TurismoLang

import sys

def inicio():
    print('¡Bienvenido al Tour Interactivo de la Ciudad!')
    print('Elige dónde quieres ir primero')
    opcion = input('Ir al cafe / Visitar el museo / Ir al parque / Ir al teatro -> ')
    if opcion == 'Ir al cafe':
        return cafe()
    if opcion == 'Visitar el museo':
        return museo()
    if opcion == 'Ir al parque':
        return parque()
    if opcion == 'Ir al teatro':
        return teatro()
    print('Opción no válida, intenta de nuevo.')
    return inicio()

def cafe():
    print('Estás en una acogedora cafetería del centro.')
    print('Huele delicioso a café recién molido.')
    opcion = input('Tomar un café y volver al inicio / Ir a la biblioteca -> ')
    if opcion == 'Tomar un café y volver al inicio':
        return inicio()
    if opcion == 'Ir a la biblioteca':
        return biblioteca()
    print('Opción no válida, intenta de nuevo.')
    return cafe()

def museo():
    print('Has llegado al museo de arte.')
    print('Hay una exposición de arte moderno.')
    opcion = input('Ir a la biblioteca / Regresar al inicio -> ')
    if opcion == 'Ir a la biblioteca':
        return biblioteca()
    if opcion == 'Regresar al inicio':
        return inicio()
    print('Opción no válida, intenta de nuevo.')
    return museo()

def parque():
    print('Estás en el parque principal de la ciudad.')
    print('Hay familias disfrutando y niños jugando.')
    opcion = input('Ir al zoologico / Regresar al inicio -> ')
    if opcion == 'Ir al zoologico':
        return zoologico()
    if opcion == 'Regresar al inicio':
        return inicio()
    print('Opción no válida, intenta de nuevo.')
    return parque()

def teatro():
    print('Llegaste al teatro municipal.')
    print('Están presentando una obra clásica.')
    opcion = input('Ir al cafe / Volver al inicio -> ')
    if opcion == 'Ir al cafe':
        return cafe()
    if opcion == 'Volver al inicio':
        return inicio()
    print('Opción no válida, intenta de nuevo.')
    return teatro()

def biblioteca():
    print('Estás en la biblioteca pública. Por favor, guarda silencio.')
    print('Hay libros de historia, ciencia y ficción.')
    opcion = input('Ir al museo nuevamente / Volver al inicio -> ')
    if opcion == 'Ir al museo nuevamente':
        return museo()
    if opcion == 'Volver al inicio':
        return inicio()
    print('Opción no válida, intenta de nuevo.')
    return biblioteca()

def zoologico():
    print('Bienvenido al zoológico!')
    print('Puedes ver leones, jirafas y pingüinos.')
    opcion = input('Regresar al parque / Volver al inicio -> ')
    if opcion == 'Regresar al parque':
        return parque()
    if opcion == 'Volver al inicio':
        return inicio()
    print('Opción no válida, intenta de nuevo.')
    return zoologico()

if __name__ == '__main__':
    inicio()