from microbit import (
    display, temperature, accelerometer, Image, sleep,
    button_a, button_b, running_time)
import random
import speech
import music
import gc

quiet = False

display.scroll('i love you')


def choose(choices, data=None):
    """ make a choice """
    if data:
        return data

    return choices[random.randint(0, len(choices) - 1)]


def say_something_simple():
    """ ernie wise """
    if random.random() < 0.6:
        display.scroll(choose(sayings))
    else:
        if random.random() < 0.1:
            sing()
        else:
            talk()


sayings = [
    "How hot is it?",
    "r and b",
    "b and b",
    "four more runs",
    "catch",
    "what time is tea?",
    "howzat!",
    "stumps",
]


def data():
    """ return some random? data """
    label, function = choose(inputs)

    out = choose(outputs)
    out(label)
    out(str(function()))


def get_songs():
    """ set up some songs """
    songs = []
    for item in dir(music):
        print(item, type(item))
        song = getattr(music, item)
        if isinstance(song, tuple):
            songs.append(song)

    return songs


songs = get_songs()


def sing(song=None):
    """ sing something simple """
    song = choose(songs, song)
    
    if quiet:
        display.scroll(song)
    else:
        music.play(song)


def pronounce(text=None):
    """ translate and pronounce """
    text = choose(sayings, text)

    speech.pronounce(speech.translate(text))


def scroll(text):
    display.scroll(text)


def talk(text=None):
    """ talk to the world """
    text = choose(sayings, text)

    gc.collect()
    if quiet:
        display.scroll(text)
    else:
        speech.say(text)


def uptime():
    """ how long have i been awake? """

    return running_time() / 1000.


def message(text=None):
    """ message in a bottle """
    import radio
    message = choose(sayings, text)

    radio.on()
    radio.send(message)
    radio.off()


def alert():
    """ check for messages """
    import radio
    radio.on()

    sleep(random.randint(10, 20))

    info = radio.receive()

    if info is None:
        info = "no messages"

    return info


inputs = [
    #'Radio alert', alert),
    ('Temp in centigrade', temperature),
    ('waves to crowd:', accelerometer.current_gesture),
    ('uptime in seconds', uptime)]


outputs = [
    #message,
    sing,
    scroll,
    talk,
    #pronounce
    ]


actions = [
    say_something_simple,
    data]


def do_something():
    """ time to do something """
    choose(actions)()


def main():

    print('hello world')
    display.show(Image.HEART)
    sleep(random.randint(0, 10) * 1000)

    if button_a.was_pressed():
        global quiet
        quiet = not quiet
        do_something()

    if button_b.was_pressed():
        sing()
        do_something()
        #music.play(music.BIRTHDAY)

    wave = accelerometer.current_gesture()
    if wave != '':
        do_something()

    gc.collect()


while True:
    try:
        main()
    except MemoryError as e:
        print(e)
        print("memory:", gc.mem_free())
        gc.collect()
