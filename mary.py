from microbit import *
import random
import speech
import music
display.scroll('i love you')

def say_something_simple():
    
    n = len(sayings)
    display.scroll(sayings[random.randint(0, n-1)])
    
sayings = [
"How hot is it?",
"Go N Z with the red hat",
"U S A",
"push those pedals",
"flags are waving",
"what time do we eat?",
"oracle with the blue hat",
]

def data():
    
    n = len(inputs)
    
    choice = random.randint(0, n-1)
    
    label, function = inputs[choice]
    
    out = random.randint(0, len(outputs) - 1)
    out = outputs[out]
    out(label)
    out(str(function()))

def get_songs():
    
    songs = []
    for item in dir(music):
        print(item, type(item))
        song = getattr(music, item)
        if isinstance(song, tuple):
            songs.append(song)
            
    return songs

songs = get_songs()

def sing(song):
    
    song = random.randint(0, len(songs)-1)
    
    music.play(songs[song])

def scroll(text):
    display.scroll(text)
    
def talk(text):
    
    speech.say(text)

outputs = [
    sing,
    scroll,
    talk]

def uptime():
    
    return running_time() / 1000.

inputs = [
    ('Temp(C):', temperature),
    ('waves:', accelerometer.current_gesture),
    ('uptime', uptime),
    
    ]
   
actions = [
    say_something_simple,
    data,
]

def do_something():
    
    action = random.randint(0, len(actions)-1)
    print('action:', action)
    actions[action]()

while True:
    
    print('hello world')
    display.show(Image.HEART)   
    sleep(random.randint(0, 10) * 1000)

    if button_a.was_pressed():
        print('button a')
        do_something()
    
    if button_b.was_pressed():
        
        print('button b')
        do_something()
     
    wave = accelerometer.current_gesture()
    print(wave)
    if wave != '':
        display.scroll(str(wave))
        do_something()
        
