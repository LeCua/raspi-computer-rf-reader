# import time

# NULL_CHAR = chr(0)

# def write_report(report):
#     with open('/dev/hidg0', 'rb+') as fd:
#         fd.write(report.encode())

# def send_key_report(key_code, modifier=0):
#     press_report = NULL_CHAR * 2 + chr(key_code) + NULL_CHAR * 5
#     release_report = NULL_CHAR * 8
#     if modifier:
#         write_report(chr(modifier) + NULL_CHAR + chr(key_code) + NULL_CHAR * 5)
#     else:
#         write_report(press_report)    
#     time.sleep(0.1)  # Add a small delay to simulate key press
#     write_report(release_report)

# # def send_text(text):
# #     for char in text:
# #         if char.isupper():
# #             send_key_report(ord(char.lower()), 2)  # Press SHIFT key
# #             send_key_report(ord(char.lower()), 0)  # Release SHIFT key and press the character key
# #         else:
# #             send_key_report(ord(char))
# def send_text(text):
#     for char in text:
#         modifier = 0
#         if char.isupper():
#             # // modifier = 2  # Set modifier to 2 for uppercase letters
#             modifier = 32  # Set modifier to 2 for uppercase letters
#             char = char.lower()
#         elif char.isdigit():
#             modifier = 4  # Set modifier to 4 for numbers
#         print     
#         send_key_report((char), modifier)
#         write_report(NULL_CHAR * 8)  # Release all keys at the end

# def send_enter_key():
#     send_key_report(40)  # Press RETURN/ENTER key

# def send_space_key():
#     send_key_report(44)  # Press SPACE key



# def send_text_with_enter(text):
#     trimmed_text = text.strip()
#     if trimmed_text:
#         send_text(trimmed_text)
#         send_enter_key()
#     else:
#         pass  # Do nothing if the input is an empty string

# if __name__ == "__main__":
#     # Example usage:
#     send_text_with_enter("   hello   ")  # Will send "hello" followed by ENTER key

#!/usr/bin/env python3

NULL_CHAR = chr(0)

def write_report(report):
   with open('/dev/hidg0', 'rb+') as fd:
       fd.write(report.encode())

def send_text_with_enter(text):
   """Sends the given text, followed by an ENTER keystroke.

   Strips any leading/trailing whitespace and only sends the text if it's not empty.
   """

   text = text.strip()
   if text:
       for char in text:
            if char.isupper():
                write_report(chr(32)+NULL_CHAR+chr(ord(char) - 93)+NULL_CHAR*5)
            else:                  
                write_report(NULL_CHAR * 2 + chr(ord(char) - 93) + NULL_CHAR * 5)
                write_report(NULL_CHAR * 8)  # Release keys
       write_report(NULL_CHAR * 2 + chr(40) + NULL_CHAR * 5)  # Press ENTER
       write_report(NULL_CHAR * 8)  # Release keys

if __name__ == '__main__':
    send_text_with_enter("AaBdCCC")  # Sends "This is a test"
#    send_text_with_enter("Hello, world!")
#    send_text_with_enter(" ")  # Sends nothing (empty string after stripping)
#    send_text_with_enter("  This is a test  ")  # Sends "This is a test"
ord("a")