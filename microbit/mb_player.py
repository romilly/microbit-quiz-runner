from microbit import *
import radio, random

id = random.randrange(1000000, 2000000)
radio.on()

while True:
    if button_a.was_pressed():
        radio.send('%d' % id)
        sleep(100)