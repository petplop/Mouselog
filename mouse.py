import subprocess
import colorama
import requests
import base64
import os
from pynput import Listener
import logging

logging.basicConfig(filename="mouse_log.txt",
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        logging.info(
            'Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

# dx is horizontal scroll
# dy is vertical


def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    logging.info(
        'Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


listener = Listener(
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()

# Haven't figured this part out yet, experiment.
# while 1:
#    input('press \'enter\' to continue...')
#   exit()
