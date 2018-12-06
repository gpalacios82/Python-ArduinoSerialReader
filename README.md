### Python-ArduinoSerialReader
Conectamos mediante python a la placa arduino con sensor de temperatura y humedad

Básicamente leemos del puerto serie y separamos los parámetros que vienen.

##### En esta versión:
* Humedad
* Temperatura
* Luminosidad
* Voltaje

El buffer de entrada desde el puerto serie es:
b'Temp:21.00\xc2\xbaC;Humidity:55.00%;Luminosity:98.00%;Voltaje:4.72V\r\n'

##### Ejemplo de Salida
Conectando puerto serie . . .

Leyendo puerto serie . . .

 
La temperatura es de: 23.00 grados

La humedad es del: 43.00 %

La luminosidad es del: 98.00 %

El voltaje de la placa es de: 4.72 V
