/*
  comunic_serie.c
  
  Copyright 2017 valentin basel <valentinbasel@gmail.com>
  
  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.
  
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  
  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.

 */

/*
############################
#                          #
#  Comunicación Serial CDC #
#                          #
############################

Esto es una prueba de un "protocolo" para comunicar una placa ARDUINO
mediante comunicación Serie (USB_CDC).
La comunicación serie o comunicación secuencial, en telecomunicaciones 
e informática, es el proceso de envío de datos de un bit a la vez, de 
forma secuencial, sobre un canal de comunicación o un bus.
El hardware ARDUINO emula el clasico protocolo de comunicación serial 
(RS232) mediante el protocolo CDC (communications device class)
que viene definido en el estanda USB.

Este pequeño proyecto, permite controlar el pin 13 de las placas ARDUINO
LEONARDO (ON/OFF), y recibir datos del sensor analogico (A0).
*/
void setup() 
  {
    /*
    El baudio (en inglés baud) es una unidad de medida utilizada en 
    telecomunicaciones, que representa el número de símbolos por 
    segundo en un medio de transmisión digital.1 Cada símbolo puede 
    comprender 1 o más bits, dependiendo del esquema de modulación.
    Es importante resaltar que no se debe confundir la velocidad en 
    baudios (baud rate) con la tasa de bits (bit rate), ya que cada 
    evento de señalización (símbolo) transmitido puede transportar uno 
    o más bits. Solo cuando cada evento de señalización (símbolo) 
    transporta un solo bit coinciden la velocidad de transmisión de 
    datos en baudios y en bits por segundo. Las señales binarias tienen 
    la tasa de bit igual a la tasa de símbolos (rb = rs), con lo cual 
    la duración de símbolo y la duración de bit son también 
    iguales (Ts = Tb). 
    */
    Serial.begin(9600);// ajusta la cantidad de bits que se envian por segundos (BAUDIOS)
    Serial.setTimeout(5);// ajusta la cantidad maxima de milisegundos para esperar datos desde el puerto serie
    pinMode(13, OUTPUT); //ajusto como salida el pin13 de la placa arduino
  }

void loop() 
  {
    /*
     El protocolo que establecemos es muy sencillo, cada ves que
     recibamos un caracter del puerto serie, lo comparamos con la
     instrucción switch y si el caracter recibido es la letra "a" ponemos el pin13 en HIGH
     (5 volt).Con la letra "b" el pin13 lo ponemos en LOW (0 volt).
     La letra "c" envia el valor del sensor analogico 0 (a0).
    */
  char dato; // variable donde se guarda el caracter ascii recibido por el puerto
  int sensor1 = 0; // varaible donde almacenamos el valor del sensor analogico
  const int analogInPin = A0; // sensor analogico A0
  if(Serial.available() > 0) // si detectamos datos en el puerto serie 
    {
      dato=Serial.read(); // guardo el caracter ASCII del puerto serie
      switch (dato) 
        {
          case 'a':
                    digitalWrite(13, HIGH); // enciendo el pin13
                    break;
          case 'b':
                    digitalWrite(13, LOW); // apago el pin13
                    break;
          case 'c':
                    sensor1 = analogRead(sensor1); // guardo el valor A0
                    Serial.println(sensor1); // envio el valor de A0 
                    break;
        }
      }
  }

