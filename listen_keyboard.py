from evdev import InputDevice, categorize, ecodes

# Replace "/dev/input/event3" with the actual device path from your system
dev = InputDevice("/dev/input/event3")

print("Listening for events...")
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        if key_event.keystate == key_event.key_up:
            print(f"Key released: {key_event.keycode}")
        elif key_event.keystate == key_event.key_down:
            print(f"Key pressed: {key_event.keycode}")