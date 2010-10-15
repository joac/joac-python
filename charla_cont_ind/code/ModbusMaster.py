#!-*- coding: utf8 -*-
"""Un Maestro Modbus de Ejemplo"""

import modbus_tk
from modbus_tk.defines import *
import modbus_tk.modbus as modbus
import modbus_tk.modbus_tcp as modbus_tcp
import time
import threading

def main():
    try:
        #Creamos la conexión con el servidor
        master = modbus_tcp.TcpMaster(port=8502, timeout_in_sec=10.0)
        #Iniciamos un ciclo de adquisicion de datos
        while True
            # Leemos las bobinas
            coils = master.execute()
            print 
            # Leemos las entradas analogicas
            analog_inputs = master.execute()
            # Leemos los registros 
            analog_registers = master.execute()
            # Dormimos un ratito
            time.sleep(0.1)
            
    finally:
        master.stop()

if __name__ == '__main__':
    "Maestro Modbus"


