#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2017 valentin basel <valentinbasel@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import serial
import time


# Esta es una clase para poder comunicar via 
# el puerto USB (usando protcolo CDC)
# es una clase muy sencilla que inicia la comunicación CDC usando
# python-serial y un sencillo protocolo para comuncarse con el firmware
# previamente cargado en la palca Arduino UNO.

# El firmware cargado en la placa Arduino solo reconoce 3 comandos
# la letra 'a' = pone en HIGH el pin 13
# la letra 'b' = pone en LOW el pin 13
# la letra 'c' = lee el puerto analogico A0 y envia el valor en formato INT
class Arduino:
    """
    API para poder interactuar con el firmware arduino.
    su funcion es la de preparar el puerto /devttyUSB o ttyACM para enviar
    y recibir datos.
    una ves inicializada la clase, hay que tener en cuenta lo siguiente:
    la variable PUERTO, es donde se carga el valor del dispositivo serie.
    por defecto es /dev/ttyACM0. cambiarla antes de usar la funcion iniciar()
    """
    PUERTO = '/dev/ttyACM0'  # valor inicial por defecto
    BAUDIOS = 9600
    BYTESIZE = 8
    PARITY = 'N'
    STOPBIT = 1
    TIMEOUT = None
    XONXOFF = True
    RTSCTS = True
    DSRDTR = True
    RS232 = serial.Serial()

    def __init__ (self):
        """
        cuando instanciamos la clase Arduino, se llama la función init
        y este llama a la función self.iniciar()
        """
        self.iniciar()

    def iniciar(self):
        """
        abre el puerto, ajusta todos los valores por defecto.
        sus variables por defecto son:
        PUERTO='/dev/ttyUSB0' # valor inicial por defecto
        BAUDIOS=9600
        BYTESIZE=8
        PARITY='N'
        STOPBIT=1
        TIMEOUT=1
        XONXOFF=False
        RTSCTS=False
        DSRDTR=False
        RS232=serial.Serial()
        Retorna -True- si funciono, -False- si hubo un error.
        no lleva argumentos
        """
        self.RS232.port = self.PUERTO
        self.RS232.baudrate = self.BAUDIOS
        self.RS232.bytesize = self.BYTESIZE
        self.RS232.parity = self.PARITY
        self.RS232.stopbit = self.STOPBIT
        self.RS232.timeout = self.TIMEOUT
        self.RS232.xonxoff = self.XONXOFF
        self.RS232.rtscts = self.RTSCTS
        self.RS232.dsrdtr = self.DSRDTR
        self.RS232.exclusive = True
        self.RS232.open()
        return True

    def prender_led(self):
        if self.RS232.isOpen():
            self.RS232.write("a")
            self.RS232.flush()
    def apagar_led(self):
        if self.RS232.isOpen():
            self.RS232.write("b")
            self.RS232.flush()
    def leer_analogico(self):
        dato=0
        if self.RS232.isOpen():
            self.RS232.write("c")
            dato=int(self.RS232.readline())
            return dato


leonardo=Arduino() # creo una instancia de la clase Arduino
dato=0 # aca guardo el dato del sensor analogico que obtengo del puerto serie
for m in range(100):
    dato=leonardo.leer_analogico()
    print "el valor del sensor analogico es: ",dato
    time.sleep(0.1)
    if dato<=100:
        leonardo.prender_led()
    else:
        leonardo.apagar_led()



