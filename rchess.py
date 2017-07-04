from microbit import display, Image

import random

while True:

    pic = []
    for row in range(5):
        im = [random.randint(0, 9) for x in range(5)]
        pic.append(''.join(str(x) for x in im))

    im = Image(':'.join(pic))

    display.show(im)
