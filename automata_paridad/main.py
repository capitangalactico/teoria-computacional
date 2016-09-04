# -*- coding: utf-8 -*-
from __future__ import print_function
from automata_paridad import ejecutar_automata
import random
# >>> import pdb
# >>> a="a string"
# >>> pdb.set_trace()
# --Return--
# > <stdin>(1)<module>()->None
# (Pdb) p a
# 'a string'
# (Pdb) To continue execution use c (or cont or continue).
def iniciar():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            ejecutar_manual()
        elif opcion == 2:
            ejecutar_random()
        elif opcion == 3:
            print('Aqui va el grafico')
        else:
            print("Error")
            return 0
        print('\n')
        print('*' * 50)
        opcion = input("Reintentar s/n: ")
        if opcion.lower() != 's':
            continuar = False

def imprimir_menu():
    print('\n\n**********Menu**********')
    print("""
        1.- Entrada en consola
        2.- Random
        3.- Ver diagrama de estados
    """)
    opcion = int(input("Selecciona una opcion: "))

    return opcion

def ejecutar_random():
    i = 0
    longitud_random = random.randint(1, 10)
    numero_binario = ''
    while i < longitud_random:
        numero_binario += random.choice(['0', '1'])
        i += 1

    print("El numero aleatorio es: ", numero_binario)
    numero_binario += ' '
    provar_paridad(numero_binario)

def ejecutar_manual():
    numero_binario = input("Escribe un numero binario: ")
    numero_binario += ' '
    provar_paridad(numero_binario)

def provar_paridad(numero_binario):
    resultado = ejecutar_automata(numero_binario)
    print('\n')
    if resultado:
        print('El numero %s, es valido' % numero_binario)
    else:
        print('El numero: %s, no es valido' % numero_binario)

iniciar()