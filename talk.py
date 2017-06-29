import music
import speech
import random

from microbit import accelerometer, display, sleep

display.scroll('hello')

while True:
    
    speed = random.randint(0, 255)
    pitch = random.randint(0, 255)
    mouth = random.randint(0, 255)
    throat = random.randint(0, 255)
    
    pitch = 240
    speed = 80
    mouth = 0
    
    print(speed, pitch, mouth, throat)
    
    speech.say("i am not a dalek", 
        pitch=pitch, throat=throat,
        mouth=mouth, speed=speed)
    sleep(random.randint(1, 10) * 2000)
    
    