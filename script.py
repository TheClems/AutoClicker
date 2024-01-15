import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Configuration
START_STOP_KEY = KeyCode(char='$')
EXIT_KEY = KeyCode(char='£')
DELAY = 0.001
BUTTON = Button.left

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.event = threading.Event()

    def start_clicking(self):
        self.running = True
        self.event.set()

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False
        self.event.set()

    def run(self):
        while self.program_running:
            self.event.wait()
            if self.running:
                mouse.click(self.button)
            time.sleep(self.delay)

mouse = Controller()
click_thread = ClickMouse(DELAY, BUTTON)
click_thread.start()

def on_press(key):
    if key == START_STOP_KEY:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == EXIT_KEY:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()