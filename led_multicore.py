import machine
import utime
import _thread

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(13, machine.Pin.OUT)
led_green = machine.Pin(14, machine.Pin.OUT)
led_red = machine.Pin(15, machine.Pin.OUT)

global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
    while True:
        print("Button value: ", button.value())
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)

#_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True:
        print("do work")
        led_red.value(1)
        for i in range(10):
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
            
        global button_pressed
        button_pressed = False
    
    led_red.value(1)
    utime.sleep(1)
    led_red.value(0)

    led_green.value(1)
    utime.sleep(1)
    led_green.value(0)
