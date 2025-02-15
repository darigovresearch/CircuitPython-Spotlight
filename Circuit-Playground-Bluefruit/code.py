# This code.py file contains Spotlight code for the Circuit Playground Bluefruit

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

    if state > 15:
        state = 0

    if state == 0:
        colours = (0, 0, 0) # LEDs off
    elif state == 1:
        colours = (1, 0, 0) # LEDs red low
    elif state == 2:
        colours = (127, 0, 0) # LEDs red medium
    elif state == 3:
        colours = (85*3, 0, 0) # LEDs red max
    elif state == 4:
        colours = (1, 1, 1) # LEDs white low
    elif state == 5:
        colours = (127, 127, 127) # LEDs white medium
    elif state == 6:
        colours = (85*3, 85*3, 85*3) # LEDs white max
    elif state == 7:
        colours = (0, 0, 1) # LEDs blue low
    elif state == 8:
        colours = (0, 0, 127) # LEDs blue medium
    elif state == 9:
        colours = (0, 0, 85*3) # LEDs blue max
    elif state == 10:
        colours = (0, 1, 0) # LEDs green low
    elif state == 11:
        colours = (0, 127, 0) # LEDs green medium
    elif state == 12:
        colours = (0, 85*3, 0) # LEDs green max
    elif state == 13:
        colours = (1, 1, 0) # LEDs yellow low
    elif state == 14:
        colours = (127, 127, 0) # LEDs yellow medium
    elif state == 15:
        colours = (85*3, 85*3, 0) # LEDs yellow max

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
