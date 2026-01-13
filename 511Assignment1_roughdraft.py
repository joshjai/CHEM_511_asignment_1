from machine import Pin
import time

led = Pin(12, Pin.OUT)

button = Pin(14, Pin.IN, Pin.PULL_UP)


start = 0 #make sure time is 0
button_state = False #

while True: #keeps going forever
    if button.value() == 0 and not button_state: #button is being pressed
        button_state = True #change state to true
        start = time.ticks_ms() #start timer
        led.value(1) #turns light on
         
        
        
    elif button.value()== 1 and button_state: # button not pressed     
        button_state = False # change state to original 
        led.value(0) # LED off 
        end_time = time.ticks_ms() #release time
        
        
        delta = time.ticks_diff(end_time, start) #change in tme
        if delta >= 1000: #set long press
            print('Long')
        else:
            print('short')
        
    time.sleep_ms(20)        
        
    #else:
        #led.value(0)
        
    #time.sleep(0.1)
 
    
    