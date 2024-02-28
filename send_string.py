# send_string.py
import time
import uinput

def send_custom_string(custom_string):
    with uinput.Device([uinput.KEY_A, uinput.KEY_B]) as device:
        for char in custom_string:
            if char.isalpha():
                device.emit_click(uinput.KEY_A + ord(char.upper()) - ord('A'))
            elif char.isdigit():
                device.emit_click(uinput.KEY_1 + int(char) - 1)
            elif char == ' ':
                time.sleep(0.1)  # Add a small delay for spaces
            else:
                print(f"Unsupported character: {char}")

if __name__ == "__main__":
    custom_string_to_send = "Hello, World!"  # Replace with your desired string
    send_custom_string(custom_string_to_send)
