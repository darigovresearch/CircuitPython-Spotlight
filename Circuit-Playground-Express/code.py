# This code.py file contains Spotlight code for the Circuit Playground Express

import time
from adafruit_circuitplayground import cp

# Global variables
global_state = 0
global_brightness = (0, 0, 0)
global_sos = False


def update_brightness():
    """update_brightness is code to adjust colour and brightness depending
    on the global state"""
    state = global_state

    state = global_state + 1

    if state > 4:
        state = 0

    if state == 0:
        colours = (0, 0, 0) # LEDs off
    elif state == 1:
        colours = (85*3, 0, 0) # LEDs red
    elif state == 2:
        colours = (85, 85, 85) # LEDs white low
    elif state == 3:
        colours = (85*2, 85*2, 85*2) # LEDs white medium
    elif state == 4:
        colours = (85*3, 85*3, 85*3) # LEDs white max

    return colours, state


def run_sos(wait_time):
    """run_sos is code to flash SOS in morse code given a specific wait time

    Morse has the following conventions
    - The length of a dot is one unit
    - The length of a dash is three units
    - The space between parts of the same letter is one unit
    - The space between letters is three units
    - The space between words is seven units
    """
    cp.pixels.fill((0, 0, 0))
    time.sleep(wait_time)

    # S
    cp.pixels.fill((255, 255, 255))
    time.sleep(wait_time)
    cp.pixels.fill((0, 0, 0))
    time.sleep(wait_time)
    cp.pixels.fill((255, 255, 255))
    time.sleep(wait_time)
    cp.pixels.fill((0, 0, 0))
    time.sleep(wait_time)
    cp.pixels.fill((255, 255, 255))
    time.sleep(wait_time)

    # wait 3 units
    cp.pixels.fill((0, 0, 0))
    time.sleep(wait_time*3)

    # O
    cp.pixels.fill((255, 255, 255))
    time.sleep(wait_time*3)
    cp.pixels.fill((0, 0, 0))
    time.sleep(wait_time)
    cp.pixels.fill((255, 255, 255))
    time.sleep(wait_time*3)
    cp.pixels.fill((0, 0, 0))
    time.sleep(wait_time)
    cp.pixels.fill((255, 255, 255))
    time.sleep(wait_time*3)

    # wait 3 units
    cp.pixels.fill((0, 0, 0))
    time.sleep(wait_time*3)

    # S
    cp.pixels.fill((255, 255, 255))
    time.sleep(wait_time)
    cp.pixels.fill((0, 0, 0))
    time.sleep(wait_time)
    cp.pixels.fill((255, 255, 255))
    time.sleep(wait_time)
    cp.pixels.fill((0, 0, 0))
    time.sleep(wait_time)
    cp.pixels.fill((255, 255, 255))
    time.sleep(wait_time)

    # wait 7 units
    cp.pixels.fill((0, 0, 0))
    time.sleep(wait_time*7)


# Loop forever
while True:

    if cp.button_b:
        global_brightness, global_state = update_brightness()
        # Wait a little bit
        time.sleep(0.2)
    else:
        pass

    if cp.button_a:
        if global_sos is True:
            global_sos = False
        else:
            global_sos = True
    else:
        pass

    if global_sos is False:
        cp.pixels.fill(global_brightness)
    else:
        run_sos(0.25)
