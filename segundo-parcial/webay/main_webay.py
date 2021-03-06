# -*- coding: utf-8 -*-
from __future__ import print_function
from diagrama import Diagrama
from automata import automata

separador = '='*50

def main():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            entrada_consola()
        elif opcion == 2:
            entrada_archivo()
        elif opcion == 3:
            ver_diagrama()
        else:
            break
        print('*' * 100)
        opcion = input("Reintentar [s/n]: ")
        if opcion.lower() != 's':
            continuar = False

    print('Saliendo del programa...')

def imprimir_menu():
    print('\n\n%sMenu%s' % (separador, separador))
    print("""
        1.- Entrada en consola
        2.- Ingresar nombre del archivo
        3.- Ver diagrama de estados
        4.- Salir
    """)
    try:
        opcion = int(input("Selecciona una opcion valida: "))
        return opcion
    except Exception as e:
        print('Error ', e)
        return 0

def entrada_consola():
    texto = input("Escribe el texto: ")
    texto += ' '
    diccionario = {}
    diccionario = automata(texto)
    imprimir_diccionario(diccionario)

def entrada_archivo():
    texto = input('Escribe el nombre del archivo: ')
    i = 1
    try:
        archivo = open(texto, 'r')
    except Exception as e:
        print('Error al abrir archivo: ', e)
        return 0
    diccionario = []
    num_linea = 1
    for linea in archivo:
        diccionario.append(automata(linea))
        num_linea += 1
    while i<num_linea:
        print('\nEn la linea: ', i)
        imprimir_diccionario(diccionario[i-1])
        i +=1
    archivo.close()

def imprimir_diccionario(diccionario):
    print('\nSe encontraron %s web y %s ebays' %(diccionario['num_web'], diccionario['num_ebay']))
    print('En las posiciones:' )
    print('%s para web' %diccionario['web_pos'])
    print('%s para ebay' %diccionario['ebay_pos'])
    print('Las palabras encontradas fueron: %s' %diccionario['palabras'])

def ver_diagrama():
    print('Mostrando diagrama del autómata. Cierre la ventana para continuar')
    try:
        diagrama = Diagrama()
        diagrama.master.title('Diagrama del autómata webay')
        diagrama.mainloop()
    except Exception as e:
        print("Error", e)

main()
