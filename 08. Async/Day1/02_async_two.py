import asyncio

async def brew_coffee(name):
    print(f"Starting to brew {name}...")
    await asyncio.sleep(2)
    print(f"{name} is ready!")
    
async def main():
    await asyncio.gather(
        brew_coffee("Espresso"),
        brew_coffee("Latte"),
        brew_coffee("Cappuccino")
    )
    
asyncio.run(main())