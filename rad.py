from microbit import *
import radio
import speech
import music
import random

radio.on()

play = True

while True:
    
    if button_a.was_pressed():
        play = not play
        print('aaaaa', play)
        
    message = radio.receive()
    
    if not message: continue
    
    #display.scroll(message):
    if play:
        music.pitch(abs(int(message)) * 4, 100)