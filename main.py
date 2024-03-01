import asyncio
from send_keyboard import send_text_with_enter
from listen_keyboard import read_input
from get_prisoner_code import get_prisoner_code

async def main():
    while True:  # Infinite loop to continuously read input
        # card_code = await read_input()
        card_code = "4170614442"
        if card_code:                        
            print("Card:", card_code)
            prisoner_code = await get_prisoner_code(card_code)
            print("Prisoner:", prisoner_code)
            send_text_with_enter(prisoner_code)
            print("Send!")
            print("")
            break

if (__name__ == "__main__"):
    # Run the main asynchronous function
    asyncio.run(main())

# import pyusb
# import pyautogui
# # pip install pyautogui
# # pip install edev

# # Replace these placeholders with your actual implementation
# def connect_to_reader():
#     # Code for connecting and identifying the reader

# def read_card_data():
#     # Code for reading data from the connected reader

# def card_scanned():
#     # Replace with code checking for new card scans using the reader

# # Main loop:
# while True:
#     if card_scanned():
#         data = read_card_data()
#         # Add suffix "DEMO" to the data
#         data_with_suffix = data + " DEMO"
#         pyautogui.write(data_with_suffix)
