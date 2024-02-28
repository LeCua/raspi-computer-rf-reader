import time
import uinput

# pip3 install python-uinput
# lsmod | grep uinput
# modprobe uinput

def send_custom_string(custom_string):
  with uinput.Device([uinput.KEY_A, uinput.KEY_B, uinput.KEY_0, uinput.KEY_9]) as device:
    for char in custom_string:
      if char.isalpha():
        device.emit_click(uinput.KEY_A + ord(char.upper()) - ord('A'))
      elif char in '0123456789':  # Check for single-digit numbers
        device.emit_click((uinput.KEY_0, int(char) - 1)[0])  # Use tuple unpacking
      elif char == ' ':
        time.sleep(0.1)  # Delay for spaces
      elif char in '.!@#$%^&*()_+-={}[]|\:;"\'<,>.?/':  # Check for supported special characters
        print(f"Unsupported special character: {char}")
      else:
        print(f"Unsupported character: {char}")

if __name__ == "__main__":
  custom_string_to_send = "Hello, World! 123 This is a test.!"  # Example string
  send_custom_string(custom_string_to_send)
