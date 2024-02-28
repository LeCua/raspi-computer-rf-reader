import asyncio
from evdev import InputDevice, categorize, ecodes

# Replace "/dev/input/event3" with the actual device path from your system
dev = InputDevice("/dev/input/event3")

async def read_input():
    input_string = ""
    for event in dev.async_read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if key_event.keystate == key_event.key_down:
                key_value = ecodes.KEY[key_event.keycode] if key_event.keycode in ecodes.KEY else ""
                if key_event.keycode == "KEY_ENTER":
                    return input_string  # Return the input string when Enter is pressed
                else:
                    input_string += key_value  # Append the character to the input string

async def main():
    while True:  # Infinite loop to continuously read input
        input_value = await read_input()
        print("Input received:", input_value)

# Run the main asynchronous function
asyncio.run(main())