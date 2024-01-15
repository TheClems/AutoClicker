import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Configuration
start_stop_key = KeyCode(char='$')
exit_key = KeyCode(char='£')
delay = 0.001
button = Button.left

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.condition = threading.Condition()

    def start_clicking(self):
        with self.condition:
            self.running = True
            self.condition.notify()

    def stop_clicking(self):
        with self.condition:
            self.running = False

    def exit(self):
        with self.condition:
            self.stop_clicking()
            self.program_running = False
            self.condition.notify()

    def run(self):
        while self.program_running:
            with self.condition:
                while not self.running and self.program_running:
                    self.condition.wait()
                if self.running:
                    mouse.click(self.button)
                self.condition.wait(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()