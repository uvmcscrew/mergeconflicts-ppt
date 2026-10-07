from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key
import time

run = [False]

cps = 50


def on_press(key):
    if key == Key.f10:
        run[0] = not run[0]


listener = Listener(on_press=on_press)
listener.start()

mouse = Controller()
while True:
    if run[0]:
        mouse.click(Button.left)
    time.sleep(1 / cps
  
