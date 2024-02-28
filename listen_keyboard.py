from evdev import InputDevice
# pip install evdev
# ls /dev
# Replace with the actual device path from step 2
print("Listening for events [1]...")
dev = InputDevice("/dev/input/event3")
print("Listening for events [2]...")
# Print key information for each event 
for event in dev.read_loop():
    print("xxxxxxxxxxx")
    print(event)
    if event.type == event.type.EV_KEY:
        print(f"Key: {event.name}, State: {event.value}")
print("Listening for events [3]...")
