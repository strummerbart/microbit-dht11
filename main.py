ciclo = 0
OLED.init(128, 64)

def on_forever():
    global ciclo
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P16, True, False, True)
    dht11_dht22.select_temp_type(tempType.CELSIUS)
    if dht11_dht22.read_data_successful():
        OLED.clear()
        OLED.write_string("Temperature(C):")
        OLED.write_num_new_line(dht11_dht22.read_data(dataType.TEMPERATURE))
        OLED.write_string("Humidity(%):")
        OLED.write_num_new_line(dht11_dht22.read_data(dataType.HUMIDITY))        
        if ciclo > 4:
            basic.clear_screen()
            ciclo = 0
            led.plot(ciclo, 0)
            led.plot(ciclo, 1)
            led.plot(ciclo, 2)
            led.plot(ciclo, 3)
            led.plot(ciclo, 4)
        else:
            led.plot(ciclo, 0)
            led.plot(ciclo, 1)
            led.plot(ciclo, 2)
            led.plot(ciclo, 3)
            led.plot(ciclo, 4)
        ciclo += 1
        basic.pause(5000)
basic.forever(on_forever)
