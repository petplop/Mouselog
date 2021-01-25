from pynput import mouse
import logging

# Logging config
logging.basicConfig(filename="log.txt",
                    level=logging.INFO, format="%(asctime)s ::  %(message)s")

# Click events with logging in terminal as well as log file (log.txt, which should be in the same dir as your file)


def on_click(x, y, button, pressed):
    if pressed:
        print("Mouse clicked with {2}".format(x, y, button))
        logging.info(
            "Mouse clicked with {2}".format(x, y, button))

# dx is horizontal
# dy is vertical

# Scroll events with logging in terminal as well as log file (log.txt, which should be in the same dir as your file)


def on_scroll(x, y, dx, dy):
    print("Mouse scrolled at ({2}, {3})".format(x, y, dx, dy))
    logging.info(
        "Mouse scrolled at ({2}, {3})".format(x, y, dx, dy))


listener = mouse.Listener(
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()

while 1:
    input("press \"enter\" to continue...")
    exit()
