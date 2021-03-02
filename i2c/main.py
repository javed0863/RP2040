"""Temperature monitor"""

import machine
import utime

from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd
DEFAULT_I2C_ADDR = 0x27
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

sensor_temp = machine.ADC(4)

CONVERSION_FACTOR = 3.3 / (65535)

#file = open("temps.txt", "w")

led_red = machine.Pin(15, machine.Pin.OUT)
led_green = machine.Pin(14, machine.Pin.OUT)

led_onboard = machine.Pin(25, machine.Pin.OUT)


def leds_off():
    led_onboard.value(0)
    led_green.value(0)
    led_red.value(0)

def leds_on():
    led_onboard.value(1)
    led_green.value(1)
    led_red.value(1)

def blink():
    leds_off()
    leds_on()
    utime.sleep(.5)
    leds_off()
    utime.sleep(.5)
    leds_on()
    utime.sleep(.5)
    leds_off()

while True:
    reading = sensor_temp.read_u16() * CONVERSION_FACTOR
    temperature = 27 - (reading - 0.706)/0.001721

    if temperature <= 29.0:
        leds_off()
        led_green.value(1)
    elif temperature > 29.0:
        leds_off()
        led_red.value(1)
    else:
        leds_on()

    print(temperature)
    lcd.move_to(0,0)
    lcd.putstr("Temperature:\n"+str(temperature))
    #file.write(str(temperature))
    #file.flush()
    utime.sleep(5)


