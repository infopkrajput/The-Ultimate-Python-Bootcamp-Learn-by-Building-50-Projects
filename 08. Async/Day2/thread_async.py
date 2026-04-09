import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stocks(item):
    print(f"Checking {item}...")
    time.sleep(2) # Blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
        
    with ThreadPoolExecutor() as pool:
        results = await loop.run_in_executor(pool, check_stocks, "Apple")
        print(results)
        
asyncio.run(main())