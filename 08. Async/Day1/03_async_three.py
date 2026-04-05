import asyncio
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.text()
    print(f"Data fetched from {url} with status {response.status}")
    
async def main():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        return await asyncio.gather(*tasks)
    
asyncio.run(main())