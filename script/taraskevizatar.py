from pynput import keyboard
from latinize import latinize

control = keyboard.Controller()
writing = False
current = ''

def touch(key):
    control.press(key)
    control.release(key)

def on_release(key):
    global writing
    global current
    if writing == True:
        try:
            current += key.char
        except:
            if key == keyboard.Key.space:
                current += ' '
            elif key == keyboard.Key.enter:
                current += '\n'
            elif key == keyboard.Key.backspace:
                current = current[:-1]
    if key == keyboard.Key.home:
        writing = True
    if key == keyboard.Key.end:
        writing = False
        for i in range(len(current)):
            touch(keyboard.Key.backspace)
        control.type(latinize(current))
        current = ''
    

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()