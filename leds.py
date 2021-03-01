import machine
import utime

led_green = machine.Pin(14, machine.Pin.OUT)
led_red = machine.Pin(15, machine.Pin.OUT)

def lightsOff():
    led_green.value(0)
    led_red.value(0)
    
def lightsOn():
    led_green.value(1)
    led_red.value(1)
    
def blink():
    lightsOn()
    utime.sleep(1)
    lightsOff()
    utime.sleep(1)

def alternateSwitching():
    led_green.toggle()
    utime.sleep(1)
    led_green.toggle()
    led_red.toggle()
    utime.sleep(1)
    led_red.toggle()

# blink()

while True:
    print("Blinking !!!")
    blink()
    # alternateSwitching();
