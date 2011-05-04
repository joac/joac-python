.. -*- mode: rst -*-

=============================================
Monitoreo y Control Industrial Usando Python
=============================================


:Autor: Joaquín Sorianello <soriasoft@gmail.com>
:Twitter: @_joac
:blog: http://www.joaclandia.com.ar
:Alergias: A los Esparragos
:Fecha: 15/10/2010

PySerial
=====================================================
:url: http://pyserial.sourceforge.net/

Nos permite adquirir datos y controlar dispositivos utilizando un bus Serie RS-232 o RS-485 (entre otros)

Dispositivos
------------
* Phimetros
* Balanzas
* Conductivimetros
* Sensores ultrasónicos
* Caudalimetros

.. raw:: pdf
   
   PageBreak


Ventajas
---------
* Muchos dispositivos sencillos cuentan con terminales serie.
* No importa el tipo de Bus.
* Es sencillo realizar mockups de dispositivos serie, para la etapa de desarrollo y testing.

Desventajas
-----------
* Algunos protocolos y formatos de comunicación no están bien documentados.
* El acceso a parámetros suele ser limitado
* Generalmente no es posible tener mas de un dispositivo en el mismo bus.
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


