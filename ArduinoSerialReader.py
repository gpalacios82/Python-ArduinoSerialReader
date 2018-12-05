import serial

if __name__ == "__main__":
    try:
        print('Conectando puerto serie . . .')
        ser = serial.Serial('/dev/cu.usbmodem14201', 9600)

        print('Leyendo puerto serie . . .')
        buffer = str(ser.readline())

        position_match = buffer.find(';')
        temperature = buffer[2:position_match]
        humidity = buffer[position_match+1:buffer.__len__()-5]

        print('La temperatura es de: ' + str(temperature) + " grados")
        print('La humedad es de: ' + str(humidity) + " %")
    except:
        print('Puerto serie no disponible')
