import music
import speech
import random

from microbit import accelerometer, display, sleep

display.scroll('dr who and the daleks')

while True:
    
    speed = random.randint(0, 255)
    pitch = random.randint(0, 255)
    mouth = random.randint(0, 255)
    throat = random.randint(0, 255)
    
    #pitch = 240
    #speed = 80
    #mouth = 0
    
    print(speed, pitch, mouth, throat)
    
    message = "i am a dalek exterminate exterminate"
    
    if random.random() < 0.5:
        speech.say(message, 
            pitch=pitch, throat=throat,
            mouth=mouth, speed=speed)
        speech.say(message)
    sleep(random.randint(1, 10) * 2000)
    
    