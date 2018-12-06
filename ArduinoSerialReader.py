import serial
from lib import extra_functions

if __name__ == "__main__":
    try:
        print('Conectando puerto serie . . .')
        ser = serial.Serial('/dev/cu.usbmodem14201', 9600)

        print('Leyendo puerto serie . . .')
        buffer = str(ser.readline())

        print(" ")
        #print("Leido: " + str(buffer))

        temperature = extra_functions.recorta("Temp:", "\\xc2", buffer)
        humidity = extra_functions.recorta("Humidity:", "%;Luminosity", buffer)
        luminosity = extra_functions.recorta("Luminosity:", "%;Voltaje", buffer)
        voltaje = extra_functions.recorta("Voltaje:", "V\\r\\n", buffer)

        print('La temperatura es de: ' + str(temperature) + " grados")
        print('La humedad es del: ' + str(humidity) + " %")
        print('La luminosidad es del: ' + str(luminosity) + " %")
        print('El voltaje de la placa es de: ' + str(voltaje) + " V")
    except:
        print('Puerto serie no disponible')
