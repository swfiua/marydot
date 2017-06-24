from microbit import *
import random
import speech
import music
display.scroll('i love you')

def choose(choices):
    
    return choices[random.randint(0, len(choices) - 1)

def say_something_simple():
    
    n = len(sayings)
    
    if random.random() < 0.9:
        display.scroll(choose(sayings))
    else:
        if random.random() > 0.8:
            sing()
        else:
            talk()
    
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
    
    label, function = choose(inputs)
    
    out = choose(outputs)
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

def sing(song=None):
    
    if song is None:
        song = choose(songs)
    
    music.play(songs[song])

def scroll(text):
    display.scroll(text)
    
def talk(text=None):
    
    if text is None:
        text = choose(sayings)
 
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
    
    choose(actions)()

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
        do_something()
        
