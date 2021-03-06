#diagrama_cero_uno.py
# -*- coding: utf-8 -*-
from __future__ import print_function
import tkinter as tk

class Diagrama(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, background='white')
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.dibujarDiagrama()
        self.centrarVentana()

    def dibujarDiagrama(self):
        coordenadas = [55, 100, 155, 200]
        for x in range(3):
            self.escribirTexto(x, coordenadas)
            self.dibujarCirculo(coordenadas)
            self.dibujarFlecha([coordenadas[0]-50, 150, coordenadas[2]-100, 150])
            coordenadas[0] += 150
            coordenadas[2] += 150

        self.dibujarCirculo([coordenadas[0]-150+5, 105, coordenadas[2]-155, 195]) # circulo interior
        self.canvas.create_arc(30, 90, 90, 150, start=30, extent=235, style='arc')
        self.canvas.create_text(40, 85, text='0, 1')

    def escribirTexto(self, x, coordenadas):
        text = ''
        text_flecha =''
        if x == 0:
            text = 'q%s' % x
            text_flecha = 'Inicio'
        elif x == 1:
            text = 'q%s' % x
            text_flecha = '0'
        elif x == 2:
            text = 'q%s' % x
            text_flecha = '1'
        else:
            print('otro')

        self.canvas.create_text(coordenadas[0]+50, coordenadas[1]+50, font=('15'), text=text)
        self.canvas.create_text(coordenadas[0]-25, coordenadas[1]+40, text=text_flecha)

    def dibujarCirculo(self, arg):
        circulo = self.canvas.create_oval(arg)

    def dibujarFlecha(self, coordenadas):
        linea = self.canvas.create_line(coordenadas)
        self.canvas.create_oval(coordenadas[2]-5, coordenadas[1]-5, coordenadas[2]+5,coordenadas[1]+5, fill = 'black')

    def centrarVentana(self):
        ancho, altura = 500, 300
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho)/2
        posicion_y = (altura_pantalla - altura)/2
        self.master.geometry('%dx%d+%d+%d' % (ancho, altura, posicion_x, posicion_y))
