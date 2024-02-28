from pynput.keyboard import Key, Controller

def write_hello123():
    """Writes the text "Hello123" followed by an Enter key press."""

    keyboard = Controller()

    try:
        # Type the text "Hello123"
        keyboard.type("Hello123")

        # Press and release the Enter key
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    write_hello123()
