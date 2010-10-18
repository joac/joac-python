#!-*- coding: utf8 -*-
"""Un Esclavo Modbus de ejemplo"""

import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_tcp as modbus_tcp
import time
import threading
import os

False = 0
True = 1
class PumpSys:
    def __init__(self, server):
        self.tanque_max = 100
        self.nivel = 0
        self.valvula = False
        self.bomba = False
        self.lsl = 10
        self.lsh = 70
        self.status = 0 #Definimos el estado como reposo
        self.start = False
        self.server= server
        self.update_values()
        self.create_slave()
        self.write_modbus()

    def update(self):
        #leemos los valores en el servidor modbus
        self.read_modbus()
        #Emulación del ciclo del plc
        if self.start:
            if self.nivel <= self.lsh and not self.bomba and not self.valvula:
                self.valvula = True
                self.status = 1 #Definimos el estado como llenando
                print "llenando"
            if self.nivel <= self.lsh and self.valvula:
                self.nivel += 1
                print "Nivel: %d litros de %d" % (self.nivel, self.tanque_max)
            if self.nivel >= self.lsh:
                self.valvula = False
                self.bomba = True
                self.status = 3 #Definimos el estado como vaciando
                print "vaciando"
            if self.bomba and self.nivel > self.lsl:
                self.nivel -= 1
                print "Nivel: %d litros de %d" % (self.nivel, self.tanque_max)
            if self.nivel <= self.lsl:
                self.bomba = False
        
        
        else:
            self.status = 0
            print "reposo"
        #escribimos los valores en el servidor Modbus
        self.write_modbus()

    def create_slave(self):

        self.slave = self.server.add_slave(1)
        for data_block in self.data:
            self.slave.add_block(data_block['name'], data_block['type'], 0, len(data_block['values']))

    def read_modbus(self):
        for d_block in self.data:
            for address, value in enumerate(d_block['values']):
                self.__dict__[value] ,= self.slave.get_values(d_block['name'], address, 1)

    def write_modbus(self):
        for d_block in self.data:
            self.slave.set_values(d_block['name'], 0, [self.__dict__[a] for a in d_block['values']])

    def update_values(self):
            self.data = [   {
                        'name' : 'rw_bol', 
                        'type'  : cst.COILS, 
                        'values': ['start',  'valvula', 'bomba']
                        }, {
                        'name'  : 'rw_analog', 
                        'type'  : cst.HOLDING_REGISTERS,
                        'values': ['lsl', 'lsh']
                        }, {
                        'name'  : 'r_analog',
                        'type'  : cst.ANALOG_INPUTS,
                        'values': ['status', 'tanque_max', 'nivel']
                        },
                    ]



def main():
    try: 
        server = modbus_tcp.TcpServer(address='127.0.0.1', port=8502)
        server.start()
        sistema = PumpSys(server)
        while True:
            sistema.update()
            time.sleep(0.1)
            os.system('clear')
                
    finally:
        server.stop()


if __name__ == '__main__':
   main() 



