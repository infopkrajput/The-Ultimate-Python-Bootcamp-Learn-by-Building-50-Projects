import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt_data(data):
    result = ''.join(reversed(data))
    return result

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, encrypt_data, "Credit_card_1234567890")
        print(result)

asyncio.run(main())