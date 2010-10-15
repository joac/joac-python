#! -*- coding: utf8 -*-

#Emulador de salida serie de balanza NC3M

import serial
import struct
import time
import random

def nc3m_from_float(numero):
    """Toma un número y retorna una cadena numerica en formato nc3m"""
    # convertimos el numero en una cadena y reemplazamos
    # el punto por una coma ','
    a = str(numero).replace('.',',')
    
    #Nos fijamos los  
    if not (',' in a):
        a += ','
    if len(a) == 7:
        return a[0:7]
    elif len(a) < 7:
        return a.zfill(7)

def fixed_rand_float(signed=False):
    "Retorna un numero con formato nc3m, por default, sin signo"
    seed = [a for a in str(random.randint(1,9999999)).zfill(7)]
    #coma_position = random.randint(0, len(seed)-1)
    coma_position = -3
    seed[coma_position]=','
    a = ''.join(seed)
    if len(a) < 7:
       a = a.zfill(7)
    if signed:
        a = random.choice([' ', ' ', ' ', '-']) + a
    print a
    return a
    
def main():

    #Definimos la estructura de salida
    fmt = "c8sc7s2c"
    
    #Tara por default
    tara = 200.0
    
    #Posibles estatus
    status = ['M', 'O', ' ']
    
    #Establecemos la conexion Serie
    ser = serial.Serial('vserial1')
    
    while True:
        s_data = struct.pack(fmt, '2', 
                            fixed_rand_float(True),
                            random.choice(status),
                            fixed_rand_float(),
                            '\r',
                            '\n',
                            )
        ser.write(s_data)
        time.sleep(1)
    
if __name__ == "__main__":
    print "Emulando Balanza NC3M"
    main()

