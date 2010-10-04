=============================================
Ejemplo de Comunicación con una Balanza NC3M
=============================================

Esta balanza de la empresa argentina industrias tecnológicas establece un formato propio para leer su salida de datos por puerto serie.

Formato del Dato
=================

<STX><SIGNO><NETO><STATUS><TARA><CR/LF>

Donde:
<STX> = 0x32 (decimal)(un byte)
<SIGNO> = 0x20 (' ') (peso Positivo) o 0x2D (Peso negativo)
<NETO> = 6 caracteres mas el punto decimal, (7 Bytes)
<STATUS> =  
        'O'(0x4f) = Sobrecarga
        'M'(0x4d) = Movimiento
        ' '(0x20) = Pesada Valida
<TARA> = mismo formato que neto
<CR/LF> Retorno de Carro y salto de Linea 0x0D 0x0A

Como se desempaqueta con struct?
==================================

.. code-block:: python-console

    >>> import struct
    >>> 
    >>> #El dato que vamos a desempaquetar
    ... data = '2 12345,6M000000,\r\n'
    >>> 
    >>> #definimos el string de formato
    ... fmt = 'c8sc7s2c'
    >>>
    >>> #desempaquetamos
    ... a = struct.unpack(fmt, data)
    >>> a
    ('2', ' 12345,6', 'M', '00000,\x00', '\r', '\n')


