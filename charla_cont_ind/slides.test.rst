.. -*- mode: rst -*-

.. |cc| image:: src/cc.large.png
    :width: 60px

.. |by| image:: src/by.large.png
    :width: 60px

.. |sa| image:: src/sa.large.png
    :width: 60px

.. |nc| image:: src/nc.large.png
    :width: 60px

=============================================
Monitoreo y Control Industrial Usando Python
=============================================

.. class:: centered

    PyCon Argentina 2010
    Córdoba


:Autor: Joaquín Sorianello <soriasoft@gmail.com>
:Fecha: 16/10/2010
:Licencia: |cc| |by| |sa| CC-by-sa-2.5

En python
=========

.. code-block:: python
    :include: code/NC3M_client.py

ModbusTk
========

ModbusTk, es un toolkit para comunicarse con dispositivos de campo, utilizando el protocolo Modbus, ya sea RTU o TCP/IP y para crear dispositivos virtuales (Muy útil para realizar mockups)

Como funciona Modbus (en forma muy general)
----------------------------------------------

Modbus tiene una arquitectura Maestro-Esclavo, donde un único dispositivo Maestro recoge datos y establece parámetros en los dispositivos Esclavos.
Establece en los dispositivos cuatro tipos de registros:

* Discretas
    - Solo lectura
    - lecto-escritura
* Analógicas
    - solo lectura
    - lecto-escritura.

Ademas establece códigos de funciones, para realizar operaciones en dichos registros

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
* ModbusRTU no soporta Mulimaster.

Ejemplo
-------
Tanque con sensor ultrasónico, una válvula y una bomba, gobernado por un PLC

.. image:: src/ejemplo2.png
    :width: 80%  
 

OpenOPC
=======

Es un toolkit OPC-DA para python.

Que es OPC?
-----------
Es el acrónimo para Object Linking and Embedding (OLE) for Process Control.
Es un estándar que permite la comunicación en tiempo real entre aplicaciones de distintos fabricantes.
Los datos se obtienen a través de *Servidores OPC*
Hay varias versiones, pero la mas utilizada es OPC-DA (fuertemente atada a Window$, ya que utiliza DCOM)

Ventajas
--------
* No tenemos que preocuparnos en la comunicación explicita con los dispositivos.
* Es sencillo de utilizar.
* Podemos acceder a muchos dispositivos con diversos protocolos, con una interfaz común.
* Es la única forma (estable) que encontré para comunicarme con dispositivos Siemens de gama media/baja.
* OpenOPC puede ser utilizado para acceder de forma remota a servidores OPC utilizando PyRO

Desventajas
-----------
* Los Servidores suelen ser pagos (y bastante caros)
* Necesitamos un equipo con windows

Ejemplo
-------
TODO

Otros módulos de comunicaciones
===============================


Porque Python
=============
Su gran cantidad de modulos:

* Toolkits Graficos
    - PyQt
    - PyGTK
    - WxPython
* Herramientas para Graficación:
    - MatplotLib
* ORMs
    - Sql Alchemy
    - Elixir
* Frameworks Web
    - Django
    - Bottle

* Twisted

Que permiten crear soluciones sofisticadas e innovadoras en materia de supervisión y control industrial

¿Preguntas?
===========

.. image:: src/question.jpg
   :width: 80%

|cc| |by| |nc| http://www.flickr.com/photos/stu_p/



 
