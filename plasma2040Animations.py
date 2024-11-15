import plasma
import random
import time
from plasma import plasma2040

NUM_LEDS = 200

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)

led_strip.start()

for i in range(NUM_LEDS):
    led_strip.set_rgb(i, 0, 0, 0)
    
def clear():
    for i in range(NUM_LEDS):
        led_strip.set_rgb(i, 0, 0, 0)
    
    
def red():
    for i in range(NUM_LEDS):
        led_strip.set_rgb(i, 255, 0, 0)
        
def random_col():
    for i in range (NUM_LEDS):
        led_strip.set_rgb(i, random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        
def cycle_random_colour():
    while True:
        random_col()
        time.sleep(0.1)
        
        
def drip(r,g,b):
    for i in range (NUM_LEDS):
        led_strip.set_rgb(NUM_LEDS - i, r, g, b)
        time.sleep(0.01)
        led_strip.set_rgb(NUM_LEDS - i , 0,0,0)
        
def rainbow_drip():
    while True:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        drip(r,g,b)

        
def rainbow_fill_drain():
    colour_list = []
    count = 0
    for i in range (NUM_LEDS):
        colour_list.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    for i in colour_list:
        led_strip.set_rgb(NUM_LEDS-count, i[0], i[1], i[2])
        count = count + 1
        time.sleep(0.1)
    count = 0
    for i in colour_list:
        led_strip.set_rgb(NUM_LEDS-count, 0, 0, 0)
        count = count + 1
        time.sleep(0.1)
    

def rainbow_pour():
    colour_list = [
        [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        for _ in range(NUM_LEDS)]
    for _ in range(NUM_LEDS):
        for index, (r, g, b) in enumerate(colour_list):
            led_strip.set_rgb(index, r, g, b)
        colour_list = [[0, 0, 0]] + colour_list[:-1]
        time.sleep(0.1)
    