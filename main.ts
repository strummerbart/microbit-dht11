let ciclo = 0
OLED.init(128, 64)
basic.forever(function on_forever() {
    
    dht11_dht22.queryData(DHTtype.DHT11, DigitalPin.P16, true, false, true)
    dht11_dht22.selectTempType(tempType.celsius)
    if (dht11_dht22.readDataSuccessful()) {
        OLED.clear()
        OLED.writeString("Temperature(C):")
        OLED.writeNumNewLine(dht11_dht22.readData(dataType.temperature))
        OLED.writeString("Humidity(%):")
        OLED.writeNumNewLine(dht11_dht22.readData(dataType.humidity))
        if (ciclo > 4) {
            basic.clearScreen()
            ciclo = 0
            led.plot(ciclo, 0)
            led.plot(ciclo, 1)
            led.plot(ciclo, 2)
            led.plot(ciclo, 3)
            led.plot(ciclo, 4)
        } else {
            led.plot(ciclo, 0)
            led.plot(ciclo, 1)
            led.plot(ciclo, 2)
            led.plot(ciclo, 3)
            led.plot(ciclo, 4)
        }
        
        ciclo += 1
        basic.pause(5000)
    }
    
})
