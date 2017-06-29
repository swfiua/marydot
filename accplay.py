import radio

import random

from microbit import accelerometer, sleep


radio.on()
while True:
    
    radio.send(str(accelerometer.get_x()))
    sleep(random.randint(0, 8) * 50)