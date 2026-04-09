import asyncio
import threading
import time

def background_task():
    while True:
        print("Background task is running...")
        time.sleep(2)
        
async def fetch_order():
    await asyncio.sleep(5)
    print("Order fetched!")
    
threading.Thread(target=background_task, daemon=True).start()

asyncio.run(fetch_order())