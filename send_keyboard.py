import time

NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def send_key_report(key_code, modifier=0):
    press_report = NULL_CHAR * 2 + chr(key_code) + NULL_CHAR * 5
    release_report = NULL_CHAR * 8
    if modifier:
        write_report(chr(modifier) + NULL_CHAR + chr(key_code) + NULL_CHAR * 5)
    else:
        write_report(press_report)
        time.sleep(0.1)  # Add a small delay to simulate key press
        write_report(release_report)

# def send_text(text):
#     for char in text:
#         if char.isupper():
#             send_key_report(ord(char.lower()), 2)  # Press SHIFT key
#             send_key_report(ord(char.lower()), 0)  # Release SHIFT key and press the character key
#         else:
#             send_key_report(ord(char))
def send_text(text):
    for char in text:
        modifier = 0
        if char.isupper():
            modifier = 2  # Set modifier to 2 for uppercase letters
            char = char.lower()
        elif char.isdigit():
            modifier = 4  # Set modifier to 4 for numbers
        send_key_report(ord(char), modifier)
        write_report(NULL_CHAR * 8)  # Release all keys at the end

def send_enter_key():
    send_key_report(40)  # Press RETURN/ENTER key

def send_space_key():
    send_key_report(44)  # Press SPACE key



def send_text_with_enter(text):
    trimmed_text = text.strip()
    if trimmed_text:
        send_text(trimmed_text)
        send_enter_key()
    else:
        pass  # Do nothing if the input is an empty string

if __name__ == "__main__":
    # Example usage:
    send_text_with_enter("   hello   ")  # Will send "hello" followed by ENTER key
