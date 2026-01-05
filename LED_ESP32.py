print("Hello World!")
from time import sleep_ms
from machine import Pin

led=Pin(2,Pin.OUT) #create LED object from pin2,Set,Pin2, to output
while True:
    led.value(1) #set led turn on 
    sleep_ms(40) #edit ms
    led.value(0) #set LED turn off
    sleep_ms(100)
    led.value(1) #set led turn on 
    sleep_ms(1000) #edit ms
    led.value(0) #set LED turn off
    sleep_ms(500)
    led.value(1)
    sleep_ms(3000)
    led.value(0)
    sleep_ms(1000)
    led.value(1)
    sleep_ms(20)
    led.value(0)
    sleep_ms(1000)