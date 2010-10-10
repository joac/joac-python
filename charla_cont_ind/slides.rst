.. -*- mode: rst -*-

=============================================
Monitoreo y Control Industrial Usando Python
=============================================

PyCon Argentina 2010


:Autor: Joaquín Sorianello <soriasoft@gmail.com>
:Fecha: 16/10/2010
:Licencia: Creative Commons BY SA

De que se trata todo esto
==========================
Monitoreo
---------
* Adquirir Datos
* Procesarlos
* Almacenarlos
* Mostrarlos

Control
-------
* Enviar consignas de control 
* Establecer parametros en los PLC en el campo.

Lo mas importante
=================

* La seguridad Física de las personas.
* La seguridad de las instalaciones.
* La continuidad de los Procesos.

El Modelo SCADA
===============

SCADA es el acronimo para Supervisory Control And Data Acquisition.
(Adqusición de Datos, Supervisión y Control)

Adquisición de Datos
--------------------
Es en lo que vamos a poner foco en esta charla: obtener datos del campo.

Supervisión
-----------
Monitoreo de parametros que permiten tomar desiciones (humanas o automaticas), sobre el proceso

Control
-------
Incio/Parada de Procesos, Seteo de parametros

Algunas alternativas a tener en cuenta:
=======================================

* PySerial
* ModbusTk
* OpenOpc

PySerial 
========
Nos Permite adquirir y controla dispositivos utilizando un Bus Serie RS-232 o RS-485 (Entre Otros)

Dispositivos
------------
* Phimetros
* Balanzas
* Conductivimetros
* Sensores ultrasonicos de nivel
* Caudalimetros

.. raw:: pdf
   
   PageBreak


Ventajas
---------
* Muchos dispositivos sencillos cuentan con terminales serie.
* No importa el tipo de Bus.
* Es Sencillo realizar Mockups de Dispositivos Serie, para la etapa de desarrollo y testing.

Desventajas
-----------
* Algunos Protocolos y Formatos de Comunicación no estan bien Documentados.
* El acceso a parametros suele ser limitado
* Generalmente no es posible tener mas de un dispoitivo en el mismo bus.
* Tenemos que implementar nuestro propio control de errores para los datos que llegan


.. raw:: pdf

   PageBreak

Lectura de Peso de una balanza NC3M
-----------------------------------
Esta balanza de la empresa argentina industrias tecnológicas establece un formato propio para leer su salida de datos por puerto serie.

Formato del Dato
****************
.. code-block:: text
    
    <STX><SIGNO><NETO><STATUS><TARA><CR/LF>
    
    <STX> = 0x32 (decimal)(un byte)
    <SIGNO> = 0x20 (' ') (peso Positivo) o 0x2D (Peso negativo)
    <NETO> = 6 caracteres mas el punto decimal, (7 Bytes)
    <STATUS> =  
        'O'(0x4f) = Sobrecarga
        'M'(0x4d) = Movimiento
        ' '(0x20) = Pesada Valida
    <TARA> = mismo formato que neto
    <CR/LF> Retorno de Carro y salto de Linea 0x0D 0x0A

En python
*********
.. code-block:: python
   :include: code/NC3M_client.py

ModbusTk
========

ModbusTk, es un toolkit para comunicarse con dispositivos de campo, utilizando el protocolo Modbus, ya sea RTU o TCP/IP y para crear dispositivos virtuales (Muy util para realizar mockups)

Como funciona Modbus (en forma muy general)
----------------------------------------------

Modbus tiene una arquitectura Maestro-Esclavo, donde un unico dispositivo Maestro recoje datos y establece parametros en los dispositivos Esclavos.
Establece en los dispositivos cuatro tipos de registros:

* Discretas
    - Solo lectura
    - lectoescritura
* Analogicas
    - solo lectura
    - lectoescritura.

Ventajas
--------
* El protocolo Modbus es abierto y esta completamente documentado.
* En Modbus/RTU podemos tener muchos dispositivos en el mismo bus.
* Existen conversores de ModbusRTU en ModbusTCP/IP
* Tiene control de errores.
* No depende de la plataforma
* ¿Ya dije que es un protocolo abierto?

Desventajas
-----------
* Muchos PLC (Siemens, por ejemplo) y dispositivos de gama baja no lo implementan.
* No es trivial implementarlo en sistemas embebidos.

Ejemplo
-------
TODO

OpenOPC
=======

Es un toolkit OPC para python.

Que es OPC?
-----------



 
