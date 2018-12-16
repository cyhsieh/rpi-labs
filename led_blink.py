import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(4,gpio.OUT)

led_state=False

#default button = high
old_input_state=True

'''
try:
    while True:
        new_input_state=gpio.input(18)
        #print(new_input_state)
        
        if new_input_state == False and old_input_state == True:
            led_state = not led_state
            time.sleep(0.2)
        old_input_state = new_input_state
        gpio.output(4,led_state)

finally:
    gpio.cleanup()
    print("clean up!")
'''

def ledfun(channel):
    print("button press!")
    global led_state
    led_state = not led_state
    gpio.output(4,led_state)

gpio.add_event_detect(18,gpio.RISING, callback=ledfun)


while True:
    try:
        print("working")
        time.sleep(5)
        pass
    except KeyboardInterrupt:
        break
        pass
    pass
gpio.cleanup()

