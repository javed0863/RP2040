import machine
import utime

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_external = machine.Pin(15, machine.Pin.OUT)

while True:
    led_external.value(0)
    if button.value() == 1:
       print("Button Pressed!")
       led_external.value(1)
       utime.sleep(.5)

       
