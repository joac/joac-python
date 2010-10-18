#!-*- coding: utf8 -*-
"""Un Maestro Modbus de Ejemplo"""

import modbus_tk
from modbus_tk.defines import *
import modbus_tk.modbus as modbus
import modbus_tk.modbus_tcp as modbus_tcp
import time
import threading
import os

def main():
    try:
        #Creamos la conexión con el servidor
        master = modbus_tcp.TcpMaster(port=8502, timeout_in_sec=10.0)
        
        master.execute(1, WRITE_SINGLE_COIL, 0, 1, output_value=1)

        #Iniciamos un ciclo de adquisicion de datos
        while True:
            # Leemos las bobinas
            coils = master.execute(1, READ_COILS,0, 3)
            print "Iniciado %d | Valvula %d | Bomba %d " % coils
            # Leemos las entradas analogicas
            analog_registers = master.execute(1, READ_HOLDING_REGISTERS, 0, 2)
            print "Nivel minimo %d | Nivel superior %d "  % analog_registers
            # Leemos los registros 
            analog_inputs = master.execute(1, READ_INPUT_REGISTERS, 0, 3)
            print "Status %d | Tanque Max %d | Nivel Actual %d"  % analog_inputs
            # Dormimos un ratito
            time.sleep(0.1)
            os.system('clear')
            
    finally:
        #frenamos el sistema
        master.execute(1, WRITE_SINGLE_COIL, 0, 1, output_value=0)
        print "Salimos"
        master.close()

if __name__ == '__main__':
    "Maestro Modbus"
    main()

