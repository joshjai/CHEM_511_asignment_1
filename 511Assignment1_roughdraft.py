# ---- distinguishing long from short ---
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
        if delta >= 500: #set long press
            print('Long')
        else:
            print('short')
        
    time.sleep_ms(20)        
        
    #else:
        #led.value(0)
        
    #time.sleep(0.1)
 
    #resourcesused 
    #https://www.circuits-diy.com/button-long-short-press-arduino-tutorial/#google_vignette 
    #https://docs.micropython.org/en/latest/library/time.html 
    #https://newbiely.com/tutorials/esp8266/esp8266-button-long-press-short-press
    

# --- LSSL password ---
from machine import Pin
import time

led = Pin(12, Pin.OUT)

button = Pin(14, Pin.IN, Pin.PULL_UP)



start = 0 #make sure time is 0
button_state = False #
password = ['L', 'S', 'S', 'L']
entered = []

while True: #keeps going forever
    if button.value() == 0 and button_state == False: #button is being pressed
        button_state = True #change state to true
        start = time.ticks_ms() #start timer
        led.value(1) #turns light on
        
    elif button.value()== 1 and button_state == True: # button not pressed     
        button_state = False # change state to original 
        led.value(0) # LED off 
        end_time = time.ticks_ms() #release time
        
        delta = time.ticks_diff(end_time, start) #change in time
        if delta >= 500: #set long press
            press = 'L'
            entered.append(press)
            print(press)
        
        else:
            press = 'S'
            entered.append(press)
            print(press)
        print(entered)
        if entered == password:
            print('Open Vault')
            led.value(1) #Set led turn off
            time.sleep_ms(600)
            led.value(0)
            entered = []
        elif entered != password and len(entered) == 4:
            print('Wrong Password')
            for x in range(5):
                led.value(0) #Set led turn on
                time.sleep_ms(100)
                led.value(1) #Set led turn off
                time.sleep_ms(100)
            led.value(0)
            entered = []
                          
    time.sleep_ms(20)        
