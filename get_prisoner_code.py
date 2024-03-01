import aiohttp
import asyncio

async def get_prisoner_code(card_code):
    url = 'http://nhixuan.tcn:8000/card2prisonercode?card_code=' + card_code
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    print(f'Failed to retrieve data: {response.status}')
                    return ""
    except aiohttp.ClientError as e:
        print(f'Error during HTTP request: {e}')
        return ""

async def main():
    card_code = "xxx"  # Replace "xxx" with the actual card code
    prisoner_code = await get_prisoner_code(card_code)
    print("Prisoner code:", prisoner_code)

if __name__ == '__main__':
    # Run the main asynchronous function
    asyncio.run(main())