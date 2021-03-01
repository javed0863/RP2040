import machine
import utime

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(13, machine.Pin.OUT)

while True:
    buzzer.value(0)
    if button.value() == 1:
        buzzer.value(1)
        utime.sleep(0.2)
