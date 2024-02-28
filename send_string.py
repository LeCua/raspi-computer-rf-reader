from uinput import KEY, Device
# pip3 install python-uinput
# lsmod | grep uinput
# modprobe uinput
# pip install --upgrade uinput

# Create the input device
device = Device()

# Define the string and map characters to key codes
text = "hello123"
key_map = {
    "a": KEY.KEY_A,
    "b": KEY.KEY_B,
    "c": KEY.KEY_C,
    "d": KEY.KEY_D,
    "e": KEY.KEY_E,
    "f": KEY.KEY_F,
    "g": KEY.KEY_G,
    "h": KEY.KEY_H,
    "i": KEY.KEY_I,
    "j": KEY.KEY_J,
    "k": KEY.KEY_K,
    "l": KEY.KEY_L,
    "m": KEY.KEY_M,
    "n": KEY.KEY_N,
    "o": KEY.KEY_O,
    "p": KEY.KEY_P,
    "q": KEY.KEY_Q,
    "r": KEY.KEY_R,
    "s": KEY.KEY_S,
    "t": KEY.KEY_T,
    "u": KEY.KEY_U,
    "v": KEY.KEY_V,
    "w": KEY.KEY_W,
    "x": KEY.KEY_X,
    "y": KEY.KEY_Y,
    "z": KEY.KEY_Z,
    "0": KEY.KEY_0,
    "1": KEY.KEY_1,
    "2": KEY.KEY_2,
    "3": KEY.KEY_3,
    "4": KEY.KEY_4,
    "5": KEY.KEY_5,
    "6": KEY.KEY_6,
    "7": KEY.KEY_7,
    "8": KEY.KEY_8,
    "9": KEY.KEY_9,
}

# Simulate typing each character and Enter key
for char in text:
    device.emit(KEY.KEY_DOWN, key_map[char])
    device.emit(KEY.KEY_UP, key_map[char])

device.emit(KEY.KEY_DOWN, KEY.KEY_ENTER)
device.emit(KEY.KEY_UP, KEY.KEY_ENTER)

# Close the device (optional)
device.close()
