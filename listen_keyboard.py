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
                # key_value = ecodes.KEY[key_event.keycode] if key_event.keycode in ecodes.KEY else ""
                if key_event.keycode == "KEY_ENTER":
                    return input_string  # Return the input string when Enter is pressed
                else:
                    # Attempt to extract the numeric part of the keycode and convert to number
                    try:
                        key_number = int(key_event.keycode.replace("KEY_", ""))
                        input_string += str(key_number)  # Append the number to the input string
                    except ValueError:
                        print("Invalid key format:", key_event.keycode)

async def main():
    while True:  # Infinite loop to continuously read input
        input_value = await read_input()
        if input_value:
            print("Input received:", input_value)

# Run the main asynchronous function
asyncio.run(main())