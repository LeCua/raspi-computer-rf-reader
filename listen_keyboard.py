from evdev import InputDevice, categorize, ecodes

# Replace "/dev/input/event3" with the actual device path from your system
dev = InputDevice("/dev/input/event3")

input_string = ""
print("Listening for events... (Press Enter to finish)")

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        if key_event.keystate == key_event.key_down:
            if key_event.keycode == "KEY_ENTER":
                print("Input received:", input_string)
                input_string = ""
                break  # Exit the loop when Enter is pressed
            else:
                input_string += key_event.keycode  # Append the key to the input string