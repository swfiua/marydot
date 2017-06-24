from microbit import *
import random
import speech
import music
import radio

display.scroll('i love you')


def choose(choices, data=None):
    """ make a choice """
    if data:
        return data

    return choices[random.randint(0, len(choices) - 1)]


def say_something_simple():
    """ ernie wise """
    n = len(sayings)

    if random.random() < 0.9:
        display.scroll(choose(sayings))
    else:
        if random.random() < 0.8:
            print('sing')
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
    "check mate",
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

    speech.say(text)



def uptime():
    """ how long have i been awake? """

    return running_time() / 1000.


def message(text=None):
    """ message in a bottle """
    message = choose(sayings, text)

    radio.on()
    radio.send(message)
    radio.off()


def alert():
    """ check for messages """
    radio.on()

    time.sleep(random.randint(10, 20))

    info = radio.receive()

    if info is None:
        info = "no messages"

    return info


inputs = [
    ('Radio alert', alert),
    ('Temp in centigrade', temperature),
    ('waves to crowd:', accelerometer.current_gesture),
    ('uptime in seconds', uptime)]


outputs = [
    message,
    sing,
    scroll,
    talk,
    pronounce]


actions = [
    say_something_simple,
    data]


def do_something():
    """ time to do something """ 
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

