import serial

if __name__ == "__main__":
    try:
        print('Conectando puerto serie . . .')
        ser = serial.Serial('/dev/cu.usbmodem14201', 9600)

        print('Leyendo puerto serie . . .')
        buffer = str(ser.readline())

        print(" ")
        #print("Leido: " + str(buffer))

        position_match1 = buffer.find('Temp:')
        position_match2 = buffer.find('\\xc2')
        temperature = buffer[position_match1+5:position_match2]

        position_match1 = buffer.find('Humidity:')
        position_match2 = buffer.find('%;Luminosity')
        humidity = buffer[position_match1+9:position_match2]

        position_match1 = buffer.find('Luminosity:')
        position_match2 = buffer.find('%;Voltaje')
        luminosity = buffer[position_match1+11:position_match2]

        position_match1 = buffer.find('Voltaje:')
        position_match2 = buffer.find('V\\r\\n')
        voltaje = buffer[position_match1+8:position_match2]


        print('La temperatura es de: ' + str(temperature) + " grados")
        print('La humedad es del: ' + str(humidity) + " %")
        print('La luminosidad es del: ' + str(luminosity) + " %")
        print('El voltaje de la placa es de: ' + str(voltaje) + " V")
    except:
        print('Puerto serie no disponible')
