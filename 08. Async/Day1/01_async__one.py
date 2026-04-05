import asyncio

async def brew_chai():
    print("Starting to brew chai...")
    await asyncio.sleep(2)  # Simulate brewing time
    print("Chai is ready!")

asyncio.run(brew_chai())
